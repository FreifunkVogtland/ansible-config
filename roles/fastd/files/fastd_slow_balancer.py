#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import socket
import sys

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import requests
import threading
import time
import urllib.parse

client_buffer = 3

config = {}
dataset = {}
dataset_lock = threading.Semaphore()


def allocate_client(domain_id):
    global config
    global dataset

    # NOTE dataset must already be locked

    if config['id'] not in dataset:
        return False

    if domain_id not in dataset[config['id']]:
        return False

    local_stats = dataset[config['id']][domain_id]
    if 'costs_limit' not in local_stats:
        return True

    if 'costs' not in local_stats:
        return True

    new_costs = local_stats['costs'] + config['client_cost']
    if new_costs > local_stats['costs_limit']:
        return False

    local_stats['costs'] = new_costs

    return True


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET_stats(self):
        global dataset
        global dataset_lock

        dataset_lock.acquire()
        data = json.dumps(dataset)
        dataset_lock.release()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(data.encode())

    def do_GET_stats_local(self):
        global config
        global dataset
        global dataset_lock

        dataset_lock.acquire()
        if config['id'] in dataset:
            dataset_local = dataset[config['id']]
        else:
            dataset_local = {}

        data = json.dumps(dataset_local)
        dataset_lock.release()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(data.encode())

    def do_GET_allowed(self, querystring):
        global dataset_lock

        query = urllib.parse.parse_qs(querystring)
        if 'domain' not in query:
            self.send_response(404)
            self.end_headers()
            return

        dataset_lock.acquire()
        allocated = allocate_client(query['domain'][0])
        dataset_lock.release()

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        if allocated:
            self.wfile.write(b'true')
        else:
            self.wfile.write(b'false')

    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        path = url.path

        if path == '/stats':
            return self.do_GET_stats()
        elif path == '/stats_local':
            return self.do_GET_stats_local()
        elif path == '/allowed':
            return self.do_GET_allowed(url.query)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        return


def read_fastd_stats(path):
    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(path)
        return json.load(sock.makefile())
    except:
        return {}


def active_peer_connection(peer):
    if 'connection' not in peer:
        return False

    if peer['connection'] is None:
        return False

    return True


def read_fastd_peer_num(path):
    stats = read_fastd_stats(path)
    if 'peers' not in stats:
        return 0

    return sum(active_peer_connection(peer) for (peerid, peer) in stats['peers'].items())


def recalculate_buffer_limits():
    global config
    global dataset

    if config['id'] not in dataset:
        return

    if config['client_limit'] >= 0:
        domain_max_costs = config['client_limit'] * config['client_cost']
    else:
        domain_max_costs = -1

    for domain in config['domains']:
        domain_id = domain['id']

        if domain_id not in dataset[config['id']]:
            continue

        local_stats = dataset[config['id']][domain_id]

        found = False
        min_costs = 0

        for peer in config['peers']:
            peer_id = peer['id']

            if peer_id == config['id']:
                continue

            if peer_id not in dataset:
                continue

            if domain_id not in dataset[peer_id]:
                continue

            remote_stats = dataset[peer_id][domain_id]

            if 'max_clients' not in remote_stats:
                continue

            if 'clients' not in remote_stats:
                continue

            if remote_stats['max_clients'] >= 0 and remote_stats['clients'] >= remote_stats['max_clients']:
                continue

            if 'costs' not in remote_stats:
                continue

            if not found:
                found = True
                min_costs = remote_stats['costs']

            min_costs = min(min_costs, remote_stats['costs'])

        local_cost_limit = (local_stats['clients'] + client_buffer)
        local_cost_limit *= config['client_cost']

        if not found:
            cost_limit = local_cost_limit
        else:
            cost_limit = min_costs + client_buffer * config['client_cost']

        if domain_max_costs >= 0:
            local_stats['costs_limit'] = min(cost_limit, domain_max_costs)
        else:
            local_stats['costs_limit'] = cost_limit


def gather_fastd_stats():
    global config
    global dataset
    global dataset_lock

    while True:
        dataset_local = {}

        for domain in config['domains']:
            num_clients = read_fastd_peer_num(domain['path'])
            dataset_local[domain['id']] = {
                'clients': num_clients,
                'max_clients': config['client_limit'],
                'costs': num_clients * config['client_cost'],
            }

        dataset_lock.acquire()
        dataset[config['id']] = dataset_local
        recalculate_buffer_limits()
        dataset_lock.release()

        time.sleep(5)


def get_peer_stats(peer_url):
    try:
        r = requests.get(url=peer_url)
        return r.json()
    except:
        return {}


def gather_peer_stats(peer_id, peer_url):
    global config
    global dataset
    global dataset_lock

    while True:
        dataset_remote = get_peer_stats(peer_url)

        dataset_lock.acquire()
        dataset[peer_id] = dataset_remote
        recalculate_buffer_limits()
        dataset_lock.release()

        time.sleep(5)


def main():
    global config

    if len(sys.argv) != 2:
        print('USAGE: ./fastd_slow_balancer.py config.json', file=sys.stderr)
        sys.exit(1)

    # TODO validate config
    config = json.load(open(sys.argv[1]))

    threading.Thread(target=gather_fastd_stats).start()

    for peer in config['peers']:
        threading.Thread(target=(lambda: gather_peer_stats(peer['id'], peer['url']))).start()

    server = ThreadingHTTPServer((config['listenip'], config['listenport']),
                                 HTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
