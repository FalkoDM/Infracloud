docker rm -f $(docker ps -a -q) # remove all containers
docker build -t school-library . # build the image
docker run -ti -p 5050:5050 -d --name school-library school-library # deploy /run in background