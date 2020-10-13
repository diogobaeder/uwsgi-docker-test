# uwsgi-docker-test

Just some tests with uWSGI and Docker

## Run in host computer

`$ uwsgi uwsgi-termination.ini`

## Run in Docker container

`$ docker rm uwsgi-docker-test; docker build . -t uwsgi-docker-test && docker run --name uwsgi-docker-test uwsgi-docker-test`
