#### OrderingFiltersExample

####  request type get : ascending order
        http://localhost:8000/studentapi/?ordering=city
        
#### request type get : descending order
        http://localhost:8000/studentapi/?ordering=-city
        

#### dependencies : pip install django_filter

#### create root project

        django-admin startproject orderingfilterexample

#### create an app : school

        cd orderingfilterexample
        python manage.py startapp school

#### orderingfilterexample/settings.py

        INSTALLED_APPS = [
          ...
            'rest_framework',
            'school',
            'django_filters',
        ]

        REST_FRAMEWORK = {
            'SEARCH_PARAM': 'q',
            'DEFAULT_FILTER_BACKENDS':[
                'django_filters.rest_framework.DjangoFilterBackend'
            ]
        }



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
        from rest_framework.response import Response
        from rest_framework.decorators import api_view
        from .models import Student
        from .serializers import StudentSerializer
        from rest_framework.views import APIView
        from rest_framework.generics import ListAPIView
        from rest_framework import filters

        class StudentList(ListAPIView):
          queryset = Student.objects.all()
          serializer_class = StudentSerializer
          filter_backends = [filters.OrderingFilter]
          # if you don't mention ordering_fields : ascending descending ordering works for all fields
          ordering_fields = ['name'] # works only for name
          # ordering_fields = ['name', 'city']


#### searchexactmatchexample/urls.py


        from django.contrib import admin
        from django.urls import path
        from school import views


        urlpatterns = [
                path('admin/', admin.site.urls),
                path('studentapi/', views.StudentList.as_view()),    # get request
        ]

#### testing : postman : 

1. if no ordering_fields mentioned, you can ordering filter all fields

2. ordering_fields = ['name']

      ascending / descending order only name

3. ordering_filds = ['name', 'city']

        ascending / descending order only name and city
  
4. ordering_fields = ['name', 'city', 'roll']
  
              ascending / descending order name, city and roll.

city

      ascending : get : http://localhost:8000/studentapi/?ordering=city
      descending : get : http://localhost:8000/studentapi/?ordering=-city


name

      ascending : get : http://localhost:8000/studentapi/?ordering=name
      descending : get : http://localhost:8000/studentapi/?ordering=-name


roll

      ascending : get : http://localhost:8000/studentapi/?ordering=roll
      descending : get : http://localhost:8000/studentapi/?ordering=-roll

