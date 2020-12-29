#### example for : single method handling both get post together

#### create root project

        django-admin startproject simplegetexample

#### create an app : school

        cd simplegetexample
        python manage.py startapp school

#### simplegetexample/settings.py

        INSTALLED_APPS = [
          ...
            'rest_framework',
            'school',
        ]


#### creating model : school/models.py : not used



#### register in school/admin.py  : not used



#### create and apply schema

        python manage.py makemigrations
        python manage.py migrate

#### admin user : not used

        python manage.py createsuperuser
        admin 
        c0met123

#### running server 
  
        python manage.py runserver

#### school/serializers.py : Not used


#### school/views.py

        from django.shortcuts import render
        from rest_framework.decorators import api_view
        from rest_framework.response import Response

        # handling get, post request together
        @api_view(['GET', 'POST'])
        def hello_world(request):
            if request.method == 'GET':
                return Response("request type is GET : hello world")
            if request.method == 'POST':
                return Response("request type is POST : hello world")




#### simplegetexample/urls.py

        from django.contrib import admin
        from django.urls import path
        from school import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('hello/', views.hello_world),      # using same url for both post and get request
        ]



## testing app : use postman

        post : localhost:8000/hello/ 
        get : localhost:8000/hello/
        
        
