FROM python:3.6
RUN git clone https://github.com/nikolayg/sample-python-api
COPY requirements.txt .
EXPOSE 5050
RUN pip install flask==1.0.2 flask-restplus==0.12.1 werkzeug==0.14.1>/dev/null
CMD python3 sample-python-api/src/main.py
