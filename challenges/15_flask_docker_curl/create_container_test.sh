docker-compose down # shuts down any running container
docker rm -f $(docker ps -a -q) # remove all containers
docker image rm flaskproject # remove the image
docker build -t flaskproject . # build the image
docker run -ti -p 5001:5001 -d flaskproject # deploy /run in background