#### updateviewexample : update existing record: supports put/patch request

#### put vs patch : 

        put : update all properties at the same time 
        patch: update selected properties 

#### create root project

        django-admin startproject updateviewexample

#### create an app : school

        cd updateviewexample
        python manage.py startapp school

#### updateviewexample/settings.py

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
        from rest_framework.generics import UpdateAPIView

        class StudentUpdate(UpdateAPIView):
          queryset = Student.objects.all()
          serializer_class = StudentSerializer


#### updateviewexample/urls.py

        from django.contrib import admin
        from django.urls import path
        from school import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('studentupdateapi/<int:pk>', views.StudentUpdate.as_view()),	# put/patch : update record
        ]






#### testing : postman : 

1. put : localhost:8000/studentupdateapi/6

        id : 6 : existing record
        payload : updating all fields
        
        {
            "name": "vicky rickey",
            "roll": 290,
            "city": "across city land"
        }



2. patch : localhost:8000/studentupdateapi/6 

        id : 6 : existing record 
        payload : updating only city : 
        {
            "city": "sutherland"
        }
