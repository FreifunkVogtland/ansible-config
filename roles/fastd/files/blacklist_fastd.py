#!/usr/bin/python3
# -*- coding: utf-8; -*-

import sys

blacklist = {
    'ffv': [
        # a42bb0a94a6a - 7667789886
        0xc7cd05f47d7ce0988a2168ba784612547462022b0199d246bc51ceedd7a6ea6a,
    ],
    'ffv_a': [
        # a42bb0a94a6a - 7667789886
        0xc7cd05f47d7ce0988a2168ba784612547462022b0199d246bc51ceedd7a6ea6a,
    ],
    'ffv_ae': [
        # a42bb0a94a6a - 7667789886
        0xc7cd05f47d7ce0988a2168ba784612547462022b0199d246bc51ceedd7a6ea6a,
    ],
    'ffv_b': [
        # a42bb0a94a6a - 7667789886
        0xc7cd05f47d7ce0988a2168ba784612547462022b0199d246bc51ceedd7a6ea6a,
    ],
}


def is_hexnumber(s):
    try:
        int(s, 16)
    except ValueError:
        return False

    return True


def blacklisted_key(domain, peer_key_str):
    if domain not in blacklist:
        return False

    if not is_hexnumber(peer_key_str):
        return False

    peer_key = int(peer_key_str, 16)
    return peer_key in blacklist[domain]


def main():
    if len(sys.argv) != 3:
        print("./blacklist_fastd.py DOMAIN PEER_KEY")
        sys.exit(1)

    domain = sys.argv[1]
    peer_key_str = sys.argv[2]

    if blacklisted_key(domain, peer_key_str):
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
