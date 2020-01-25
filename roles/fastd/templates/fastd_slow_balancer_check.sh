#! /bin/sh
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2017-2020, Sven Eckelmann <sven@narfation.org>

if [ "$(curl -s "http://{{ bgp_ipv4 | ipaddr('address') }}:26725/allowed?domain=$1")" = "false" ]; then
	exit 1
else
	exit 0
fi
