# online-graph-maker

Quickly create custom charts using a CSV file.


## 🚧️ Development environment

https://onlinegraphmaker-dev.herokuapp.com/

First time running heroku-deploy script:

        $ chmod +x heroku-deploy.sh


To deploy using Heroku Container Registry service (deploy pre-built Docker images):

        $ heroku container:login
        $ ./heroku-deploy.sh


### Useful Heroku CLI and Django commands

Open app

        $ heroku open -a onlinegraphmaker-dev

Django initializations

        $ heroku run python manage.py collectstatic --no-input --clear -a onlinegraphmaker-dev
        $ heroku run python manage.py makemigrations -a onlinegraphmaker-dev
        $ heroku run python manage.py migrate -a onlinegraphmaker-dev

Run console

        $ heroku run bash -a onlinegraphmaker-dev

Create super user

        $ python manage.py createsuperuser

Run psql cli

        $ heroku pg:psql postgresql-name-373 -a onlinegraphmaker-dev
