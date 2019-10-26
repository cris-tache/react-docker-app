#!/bin/bash

git clone https://github.com/cris-tache/react-docker-app.git
cd ./react-docker-app
tar -xf app.tar.xz
rm -rf app.tar.xz
cd ./app
docker build -t react-docker-app .
cd ..
docker-compose up -d
