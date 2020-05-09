FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV STATIC_PATH /app/agc_app/static

ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

ADD . /app