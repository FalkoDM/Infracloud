docker rm -f $(docker ps -a -q) # remove all containers
docker build -t school-library . # build the image
docker run -ti -d --name school-library school-library # deploy /run in background