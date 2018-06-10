#! /bin/sh

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# read new hosts/ethers
dns_pre="$(/usr/bin/git -C /opt/freifunk/dns/ rev-parse HEAD)"
/usr/bin/git -C /opt/freifunk/dns/ pull -q
dns_post="$(/usr/bin/git -C /opt/freifunk/dns/ rev-parse HEAD)"

if [ "${dns_pre}" != "${dns_post}" ]; then
	/usr/bin/killall -SIGHUP dnsmasq
fi
