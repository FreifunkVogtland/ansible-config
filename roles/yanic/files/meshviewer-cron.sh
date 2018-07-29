#! /bin/sh

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# generate new files based on the json data
/opt/freifunk/meshviewer/ffv-meshviewer-filter/filter.py /opt/freifunk/meshviewer/data/ /var/www/meshviewer/ffv/

/opt/freifunk/meshviewer/ffv-nodes2eventlog/nodes2eventlog.py /var/www/meshviewer/ffv/nodes.json /opt/freifunk/meshviewer/ffv-nodes2eventlog/db /var/www/meshviewer/ffv/eventlog.atom
OFFLINE_THRESHOLD=60 /opt/freifunk/meshviewer/ffv-nodes2eventlog/nodes2eventlog.py /var/www/meshviewer/ffv/nodes.json /opt/freifunk/meshviewer/ffv-nodes2eventlog/db-threshold60 /var/www/meshviewer/ffv/eventlog-threshold60.atom
/opt/freifunk/meshviewer/ffv-nodes2eventlog/graveyard2rst.py /opt/freifunk/meshviewer/ffv-nodes2eventlog/db-threshold60 /var/www/meshviewer/ffv/graveyard.rst
/usr/bin/pandoc -f rst -t html5 -o /var/www/meshviewer/ffv/graveyard.html /var/www/meshviewer/ffv/graveyard.rst

/opt/freifunk/ffv-api-generator/api-gen.py /var/www/meshviewer/ffv/meshviewer.json /var/www/meshviewer/ffv/
/opt/freifunk/meshviewer/meshviewer2kml/meshviewer2kml.py /var/www/meshviewer/ffv/meshviewer.json /var/www/meshviewer/ffv/nodelist.kml
