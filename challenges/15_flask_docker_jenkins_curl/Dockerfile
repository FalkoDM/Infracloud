FROM python:3
COPY . .
RUN apt-get -y update
RUN pip3 install -r requirements.txt

EXPOSE 5050

CMD python3 app/app.py
