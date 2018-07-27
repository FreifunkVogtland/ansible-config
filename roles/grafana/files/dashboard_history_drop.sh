#! /bin/sh

# prevent that the grafana.db uses all the available space
/etc/init.d/grafana-server stop
echo 'delete from dashboard_version;vacuum;'|sqlite3 /var/lib/grafana/grafana.db
/etc/init.d/grafana-server start
