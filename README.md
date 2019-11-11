# react-docker-app

  This project contains an empty react app using https://github.com/facebook/create-react-app 
The app is containerized in a Dockerfile located in the app folder.
  The deployment.py script clones the github repository, extracts the archive, builds the containers structure locally and finally tests if the containers are up and running using curl.
  The docker-compose.yml file there are 2 services defined: reactapp and mongodb. These 2 communicate between each other 
on the reactappnetwork (internal network). The reactapp code is kept in a volume.

