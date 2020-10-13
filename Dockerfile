FROM python:3.8.5

RUN mkdir /app
COPY requirements.txt /app/

WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app/

CMD uwsgi uwsgi-termination.ini
