#!/bin/bash
docker build -t postgis Docker
docker run --name postgis -p 5432:5432 -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=password -d postgis
