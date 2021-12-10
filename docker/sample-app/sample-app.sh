#!/bin/bash

# create temp directories
mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

# copy the website directories and sample_app.py to the temp directory
cp sample_app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

# create Dockerfile echo FROM python is to install python in the container
echo "FROM python" >> tempdir/Dockerfile

# use the docker RUN command to install flask in the container
echo "RUN pip install flask" >> tempdir/Dockerfile

# use the COPY command to copy the files from the tempdir to the container /home/myapp/
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY sample_app.py /home/myapp/" >> tempdir/Dockerfile

# use EXPOSE to listen for a specific port
echo "EXPOSE 8080" >> tempdir/Dockerfile

# use the CMD command to execute the python script
echo "CMD python3 /home/myapp/sample_app.py" >> tempdir/Dockerfile

cd tempdir # switch to the tempdir to create the container
docker build -t sampleapp .
 # start the container and verify it's running
 docker container run -t -d -p 8080:8080 --name samplerunning sampleapp

 # display all current running docker containers
 docker ps -a