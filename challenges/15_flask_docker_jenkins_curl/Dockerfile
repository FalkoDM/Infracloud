FROM python:latest
RUN git clone https://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@github.com/FalkoDM/infracloud.git
RUN apt-get -y update
RUN pip3 install -r /infracloud/challenges/15_flask_docker_jenkins_curl/requirements.txt 
EXPOSE 5050
CMD python3 /infracloud/challenges/15_flask_docker_jenkins_curl/app/app.py 
