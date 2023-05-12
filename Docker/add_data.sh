#!/bin/bash
echo "Begin adding data..."
osm2pgsql /tmp/poland-latest.osm.pbf --cache 4000 --slim --drop
echo "Done"
