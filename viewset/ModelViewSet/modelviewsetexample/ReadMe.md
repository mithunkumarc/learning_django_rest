#### ModelViewSet: provide crud implementation methods


#### create root project

        django-admin startproject modelviewsetexample

#### create an app : school

        cd modelviewsetexample
        python manage.py startapp school

#### modelviewsetexample/settings.py

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
        from rest_framework.viewsets import ModelViewSet

        class StudentModelViewSet(ModelViewSet):
          queryset = Student.objects.all()
          serializer_class = StudentSerializer


#### modelviewsetexample/urls.py

        from django.contrib import admin
        from django.urls import path, include
        from school import views
        from rest_framework.routers import DefaultRouter

        router = DefaultRouter()

        # you could register other apis too
        router.register('studentapi', views.StudentModelViewSet, basename="student")

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include(router.urls)),	
        ]


#### testing : postman : 

1. get: reading all records

        localhost:8000/studentapi  


2. get: single record : primary key (pk)/id of stduent:7

        localhost:8000/studentapi/7

3. put : updating all fields

        localhost:8000/studentapi/7/
        payload :
        {
            "name": "shamanth",
            "roll": 5,
            "city": "scotland west"
        }


4. patch : update only specific fields : partial update

        localhost:8000/studentapi/7/
        payload : 
        {
            "city": "scotland south"
        }

5. delete: 

        localhost:8000/studentapi/7/
