#### retrieveupdateapiview : read or update  single record/instance. supports put/patch and get request.

#### put vs patch : 

        put : update all properties at the same time 
        patch: update selected properties 

#### create root project

        django-admin startproject retrieveupdateexample

#### create an app : school

        cd retrieveupdateexample
        python manage.py startapp school

#### retrieveupdateexample/settings.py

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
        from rest_framework.generics import RetrieveUpdateAPIView

        class StudentRetrieveUpdate(RetrieveUpdateAPIView):
          queryset = Student.objects.all()
          serializer_class = StudentSerializer


#### classbasedcrudexample/urls.py

        from django.contrib import admin
        from django.urls import path
        from school import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            # supports post, patch and get(read single record)
            path('studentretrieveupdate/<int:pk>', views.StudentRetrieveUpdate.as_view()),	
        ]




#### testing : postman : 


1. reading single record : get 

      localhost:8000/studentretrieveupdate/7


2. put : updating single record. can be updated all fields 

        localhost:8000/studentretrieveupdate/7
        payload : 
        {
            "name": "shamanth prasad",
            "roll": 35,
            "city": "scotland east"
        }

3. patch : partial update record.

        localhost:8000/studentretrieveupdate/7
        payload :
        {
            "roll": 15
        }
