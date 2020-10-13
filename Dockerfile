FROM python:3.8.5

RUN pip install 'uwsgi==2.0.19.1'

RUN useradd -d /app app
WORKDIR /app
USER app
COPY --chown=app . /app/

CMD uwsgi uwsgi-termination.ini
