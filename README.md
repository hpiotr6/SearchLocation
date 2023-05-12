# SearchLocation
The repository uses the OpenStreetMap database to look for the location of given traits. Keywords: PostGIS, OpenStreetMap, Python
## Installation
```sh
# Build docker image and run. Initialising takes approx. 30 min.
. ./initialise_db.sh
```
Initializing is completed when `docker logs postgis` shows
```
2023-05-12 16:32:10.308 UTC [1] LOG:  database system is ready to accept connections
```
Python environment is managed by [Poetry](https://python-poetry.org/docs/).

## Usage
```sh
poetry shell
python main.py
```
