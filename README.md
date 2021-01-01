# learning_django_rest

#### project files checklist

        views.py                : handle requests
        serializers.py          : serializers here
        models.py               : create models here
        admin.py                : register model here
        database migrations     : run db schema
        rootproject/settings.py : install your app and rest_framework here
        urls.py                 : configure urls here

#### makemigrations vs migrate

        makemigrations : generate sql code/schema
        migrate : execute/apply sql code/creates tables


#### make use of admin UI

1. register models(entity) in yourapp/admin.py
2. in localhost:port/admin UI you can manage crud operations with your model
3. admin UI helps to test urls/views api

#### django rest flow

                request from browser => urls => views => serializers => model => database

1. urls are entry point for accessing django rest
2. views handle requests
3. views take help of serializers to convert json to python object viceversa.
4. models retrive/read and push python object to database.


#### install django filter

        pip install django-filter

#### implement topics

        https://docs.djangoproject.com/en/3.1/topics/db/
        https://docs.djangoproject.com/en/3.1/topics/
        https://bezkoder.com/django-rest-api/
