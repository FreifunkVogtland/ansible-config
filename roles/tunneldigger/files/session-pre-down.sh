#!/bin/bash

INTERFACE="$3"

ip link set dev "$INTERFACE" nomaster
exit 0
