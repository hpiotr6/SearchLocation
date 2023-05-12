FROM postgis/postgis:latest
RUN apt-get update && apt-get install -y \
    osm2pgsql \
    wget && rm -rf /var/lib/apt/lists/*
RUN wget --no-verbose --show-progress https://download.geofabrik.de/europe/poland-latest.osm.pbf -P /tmp
COPY ./add_data.sh /docker-entrypoint-initdb.d/add_data.sh
RUN chmod +x /docker-entrypoint-initdb.d/add_data.sh
