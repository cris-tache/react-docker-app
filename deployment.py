#!/usr/bin/env python
# A script to clone the app source code, builds the containers
# Before running the script create a directory for the project and cd into it. From there run deployment.py

import subprocess
import os

try:
    print("Cloning from the github repository\n")
    subprocess.call("git clone https://github.com/cris-tache/react-docker-app.git", shell=True)
except:
    print("Cannot connect to the repository, please check your internet connection and try again")

print("Extracting the archive file\n")
p = subprocess.Popen("tar -xf app.tar.xz", cwd="./react-docker-app", shell=True)
p.communicate()                      # aici mi-a luat ceva timp pana sa folosesc communicate; nu intelegeam de ce nu merge cd ./react-docker-app/app. Dar fisierul apt.tar.xz inca se dezarhiva si eu nu vedeam output-ul in consola :)
os.chdir('react-docker-app/app')

print("Building the docker image for the react-app\n")
p1 = subprocess.Popen("docker build -t react-docker-app .", shell=True)
p1.communicate()

print("Creating the docker containers using docker-compose.yml file\n")
p2 = subprocess.Popen("docker-compose up -d", cwd="..", shell=True)
p2.communicate()

# Test if the react app is running at http://localhost:8081

output = subprocess.check_output("curl http://localhost:8081 | head -n 5", shell=True)
print(output)
