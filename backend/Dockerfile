FROM python:3.8-slim-buster

EXPOSE 8000 3333

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /opt/app

COPY requirements.txt init_app.sh ./

COPY . .

RUN apt-get -q -y update \
    && apt-get -q -y install nano \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && chmod +x init_app.sh \
    && ./init_app.sh

# add and run as non-root user
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /opt/app

USER appuser

CMD gunicorn backend.wsgi --bind 0.0.0.0:$PORT
