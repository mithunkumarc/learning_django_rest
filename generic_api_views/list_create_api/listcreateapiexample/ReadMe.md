#### ListCreateAPIView : reading list of records and creating new record. support get and post request

#### create root project

        django-admin startproject listcreateapiexample

#### create an app : school

        cd listcreateapiexample
        python manage.py startapp school

#### listcreateapiexample/settings.py

        INSTALLED_APPS = [
          ...
            'rest_framework',
            'school',
        ]


#### creating model : school/models.py


        from django.db import models
        from datetime import datetime
        from django.utils.timezone import now

        # Create your models here.
        class Student(models.Model):
            name = models.CharField(max_length=50)
            roll = models.IntegerField()
            city = models.CharField(max_length=50)




#### register in school/admin.py 

        from django.contrib import admin
        from .models import Student
        # Register your models here.
        # admin.site.register(Student)

        @admin.register(Student)
        class StudentAdmin(admin.ModelAdmin):
            # list all fields in table(Admin UI)
            # id : default field created by django
            list_display = ['id', 'name', 'roll', 'city']



### create and apply schema

        python manage.py makemigrations
        python manage.py migrate

#### creating admin user

        python manage.py createsuperuser
        admin 
        c0met123

#### runserver

        python manage.py runserver

#### school/serializers.py

        from rest_framework import serializers
        from .models import Student

        class StudentSerializer(serializers.ModelSerializer):
            class Meta:
                model = Student
                fields = '__all__' # may be requesting to serialize all fields



#### school/views.py

        from django.shortcuts import render
        # from rest_framework.response import Response
        from rest_framework.decorators import api_view
        from .models import Student
        from .serializers import StudentSerializer
        from rest_framework.views import APIView
        from rest_framework.generics import ListCreateAPIView

        class StudentListCreate(ListCreateAPIView):
          queryset = Student.objects.all()
          serializer_class = StudentSerializer


#### listcreateapiexample/urls.py


        from django.contrib import admin
        from django.urls import path
        from school import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('studentlistcreate', views.StudentListCreate.as_view()),	# list: get, create: post
        ]




#### testing : postman : 


        1. post : creating new record
        localhost:8000/studentlistcreate
        payload : 
        {
            "name": "shamanth",
            "roll": 34,
            "city": "scotland"
        }

        2. get : read all records
        localhost:8000/studentlistcreate
