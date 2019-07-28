#!/bin/bash

git pull
../env/bin/python manage.py migrate
#cd frontend
#npm i
#npm run build
#cd ..
#../env/bin/python manage.py collectstatic
sudo supervisorctl restart hackathon
