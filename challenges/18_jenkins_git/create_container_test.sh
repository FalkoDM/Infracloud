#docker rm -f $(docker ps -a -q) # remove all containers
docker rm -f flaskproject
docker image rm flaskproject # remove the image
docker build -t flaskproject . # build the image
docker run -ti -p 5050:5050 -d --name flaskproject flaskproject # deploy /run in background