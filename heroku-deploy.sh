!/bin/sh

heroku login
heroku container:login
cd backend/
docker build -t registry.heroku.com/onlinegraphmaker-dev/web .
docker push registry.heroku.com/onlinegraphmaker-dev/web
heroku container:release web -a onlinegraphmaker-dev
heroku logs --tail -a onlinegraphmaker-dev
