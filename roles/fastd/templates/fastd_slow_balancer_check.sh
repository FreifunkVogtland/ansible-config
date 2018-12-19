#! /bin/sh

if [ "$(curl -s "http://{{ bgp_ipv4 | ipaddr('address') }}:26725/allowed?domain=$1")" = "false" ]; then
	exit 1
else
	exit 0
fi
