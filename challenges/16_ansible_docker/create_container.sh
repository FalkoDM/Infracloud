docker rm -f $(docker ps -a -q) # remove all containers
docker image rm apache_test # remove the image
docker build -t apache_test . # build the image
docker run -ti -p 8888:8081 -d --name apache_test apache_test # deploy /run in background