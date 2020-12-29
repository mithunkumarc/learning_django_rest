#### example to read simple get request : contains only views and urls

#### steps

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



#### register in school/admin.py : not used

#### create and apply schema 

      python manage.py makemigrations
      python manage.py migrate

#### creating admin user : not needed

        python manage.py createsuperuser
        admin 
        c0met123

#### run server : 

        python manage.py runserver

#### school/serializers.py : not used


#### school/views.py

        from django.shortcuts import render
        from rest_framework.decorators import api_view
        from rest_framework.response import Response

        #by default api view accept only get requests : @api_view(['GET'])
        @api_view()
        def hello_world(request):
          return Response("hello world")



#### simplegetexample/urls.py

        from django.contrib import admin
        from django.urls import path
        from school import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('hello/', views.hello_world),
        ]



#### testing app : use postman

        localhost:8000/hello
