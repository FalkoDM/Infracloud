FROM python:latest
RUN pip install flask && pip install datetime
COPY ./static /home/microweb_app/static/
COPY ./templates /home/microweb_app/templates/
COPY ./micro.py /home/microweb_app/
EXPOSE 5059
CMD python /home/microweb_app/micro.py