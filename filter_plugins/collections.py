# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2018-2019, Sven Eckelmann <sven@narfation.org>

from jinja2.filters import environmentfilter


@environmentfilter
def mesh_fill(env, collection, vpnid, ROUTERRANGEV6):
    meshes = {}

    for mesh_name in collection:
        meshes[mesh_name] = {}

        mesh_meta = collection[mesh_name]
        mesh = meshes[mesh_name]
        jinja_vars = {
            'vpnid': vpnid,
            'mesh_meta': mesh_meta,
            'ROUTERRANGEV6': ROUTERRANGEV6
        }

        mesh['id'] = mesh_meta['id']

        mesh['vxlan'] = {}
        mesh['vxlan']['id'] = mesh_meta['vxlan']['id']

        mesh['batadv'] = {}
        mesh['batadv']['mac'] = env.from_string("{{ '02:ba:7a:df:%02x:%02x'|format(vpnid|int, mesh_meta['id']|int) }}").render(jinja_vars)
        mesh['batadv']['brmac'] = env.from_string("{{ '06:ba:7a:df:%02x:%02x'|format(vpnid|int, mesh_meta['id']|int) }}").render(jinja_vars)
        mesh['batadv']['lladdr'] = env.from_string("{{ 'fe80::ba:7aff:fedf:%02x%02x'|format(vpnid|int, mesh_meta['id']|int) }}").render(jinja_vars)
        mesh['batadv']['primary'] = env.from_string("{{ '02:62:e7:ab:%02x:%02x'|format(vpnid|int, mesh_meta['id']|int) }}").render(jinja_vars)

        mesh['ipv4'] = {}
        mesh['ipv4']['subnet'] = env.from_string("{{ mesh_meta['ipv4']['subnet'] }}").render(jinja_vars)
        mesh['ipv4']['vpn_start'] = env.from_string("{{ mesh_meta['ipv4']['vpn_start'] }}").render(jinja_vars)
        mesh['ipv4']['client_start'] = env.from_string("{{ mesh_meta['ipv4']['client_start'] }}").render(jinja_vars)
        mesh['ipv4']['per_vpn'] = env.from_string("{{ mesh_meta['ipv4']['per_vpn'] }}").render(jinja_vars)
        mesh['ipv4']['ip'] = env.from_string("{{ mesh_meta['ipv4']['subnet'] | ipaddr(vpnid|int - 1 + mesh_meta['ipv4']['vpn_start']) | ipaddr('address') }}").render(jinja_vars)

        mesh['ipv6'] = {}
        mesh['ipv6']['prefix_64'] = env.from_string("{{ mesh_meta['ipv6']['prefix_64'] }}").render(jinja_vars)
        mesh['ipv6']['subnet'] = env.from_string("{{ ROUTERRANGEV6 | ipsubnet(64, mesh_meta['ipv6']['prefix_64']) }}").render(jinja_vars)
        mesh['ipv6']['ip'] = env.from_string("{{ ROUTERRANGEV6 | ipsubnet(64, mesh_meta['ipv6']['prefix_64']) | ipaddr(1) }}").render(jinja_vars)

        mesh['dnsmasq'] = {}
        mesh['dnsmasq']['start'] = env.from_string("{{ mesh_meta['ipv4']['subnet'] | ipaddr((vpnid|int - 1) * mesh_meta['ipv4']['per_vpn'] + mesh_meta['ipv4']['client_start']) | ipaddr('address') }}").render(jinja_vars)
        mesh['dnsmasq']['end'] = env.from_string("{{ mesh_meta['ipv4']['subnet'] | ipaddr((vpnid|int) * mesh_meta['ipv4']['per_vpn'] - 1 + mesh_meta['ipv4']['client_start']) | ipaddr('address') }}").render(jinja_vars)

    return meshes


def int_add(collection, val):
    return map(lambda x: x + val, collection)


class FilterModule(object):
    def filters(self):
        return {
            'mesh_fill': mesh_fill,
            'int_add': int_add,
        }
