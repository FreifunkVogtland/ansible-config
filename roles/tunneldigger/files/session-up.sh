#!/bin/bash

INTERFACE="$3"

ip link set dev "$INTERFACE" up mtu 1426 master tunneldigger
