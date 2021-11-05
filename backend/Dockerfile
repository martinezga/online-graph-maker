FROM python:3.8-slim-buster

EXPOSE 8000 3333

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /opt/app

COPY requirements.txt entrypoint.sh /app/

COPY . /opt/app/

RUN apt-get -q -y update \
    && apt-get -q -y install nano \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

#ENTRYPOINT ["sh", "/opt/app/entrypoint.sh"]

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]