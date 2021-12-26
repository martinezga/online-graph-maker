FROM python:3.8-slim-buster

EXPOSE 8000 3333

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /opt/app

ADD requirements.txt entrypoint.sh /opt/app/

RUN apt-get -q -y update \
    && apt-get -q -y install nano \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    # gosu installation to switch to nonroot user in entrypoint.sh
    && set -eux; \
    apt-get install -y gosu; \
    rm -rf /var/lib/apt/lists/*; \
    # verify that the binary works
    gosu nobody true

ADD ./backend /opt/app

# add and run as non-root user
RUN adduser -u 5678 --disabled-password --gecos "" appuser 

ENTRYPOINT ["sh", "./entrypoint.sh"]

CMD gunicorn backend.wsgi --bind 0.0.0.0:$PORT
