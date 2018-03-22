#! /bin/sh

# prevent that the grafana.db uses all the available space
echo 'delete from dashboard_version;vacuum;'|sqlite3 /var/lib/grafana/grafana.db
