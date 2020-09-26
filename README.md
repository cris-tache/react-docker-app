# react-docker-app

## Description
  This project contains a test app based on https://github.com/facebook/create-react-app 
The app is containerized in a Dockerfile located in the app folder.
  The deployment.py script clones the github repository, extracts the archive, builds the containers structure locally and finally tests if the containers are up and running using curl.
  The docker-compose.yml file comprises 2 services: reactapp and mongodb. These 2 communicate 
on the reactappnetwork (internal network). The reactapp code is kept in a persistent volume.

## Implementation 
This project is implemented using Docker, docker-compose, react-app and python

