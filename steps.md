# Dev & Install Steps
<font size='2'>

__Python config__

    cd -projectDir-
    python -m pipenv shell
    pip install pipenv
    pipenv install django djangorestframework django-cors-headers mysqlclient
    django-admin startproject backend
    cd backend
    python manage.py startapp copro
    python manage.py migrate
    python manage.py runserver



in settings.py :
add 'copro','corsheaders', 'rest_framework'  to __INSTALLED_APP__
add 'corsheaders.middleware.CorsMiddleware' to __MIDDLEWARE__
add at the end : #white list the frontend server

    CORS_ORIGIN_WHITELIST = [
        'http://localhost:3000'
    ]

----
__Add DB Connection__ :
1st Method :

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': '/db.cnf',
            },
        }
    }

add db.cnf file to same dir as settings.py :
my.cnf : 

    [client]
    database = db_synd
    user = db_synd
    password = db_synd
    default-character-set = utf8


OR
2nd method

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'db_synd',
                'USER': 'db_synd',
                'PASSWORD': 'db_synd',
                'HOST': '127.0.0.1',
                'PORT': '3306',
            }
        }

----
__manage db model__

import models from mysql:

    python manage.py inspectdb > models.py
register models in admin.py

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver


----
__API config__

New file corpo/serializers.py
register corpo/serializers
register corpo/views
register backend/urls
Test Django API

----
__Frontend__

    npx clear-npx-cache
    npx create-react-app frontend
    cd frontend
    npm install bootstrap@4.6.0 reactstrap@8.9.0 --legacy-peer-deps

add to index.js

    import 'bootstrap/dist/css/bootstrap.css';