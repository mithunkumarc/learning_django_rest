#### requirement dependecies: 

        python 
        django web framework 
        django rest framework 


#### creating project

        django-admin startproject gs2
        cd gs2
        python manage.py startapp api

#### add application in root project settings.py file

        # inside gs2/settings.py , installed apps array
        
          rest_framework,
          api,

#### api/models.py

        from django.db import models

        # Create your models here.
        class Student(models.Model):
            name = models.CharField(max_length=100)
            roll = models.IntegerField()
            city = models.CharField(max_length=100)


#### creating schema and applying them

        # create schema
        python manage.py makemigrations 
        # apply schema
        python manage.py migrate
        # create admin
        python manage.py createsuperuser        
        # follow instructions create admin
        # run server
        python manage.py runserver


#### register student model to admin

        # api/admin.py


        from django.contrib import admin
        from .models import Student
        # Register your models here.

        @admin.register(Student)
        class StudentAdmin(admin.ModelAdmin):
            # below fields will display in Student table, opened in admin page
            list_display = ['id', 'name', 'roll', 'city']


#### login admin, check student model in admin UI

        > localhost:8000/admin 
        > you can see student link available in admin page


#### create serializers.py file in api app

        from rest_framework import serializers
        from .models import Student

        class StudentSerializer(serializers.Serializer):
            name = serializers.CharField(max_length=100)
            roll = serializers.IntegerField()
            city = serializers.CharField(max_length=100)

            #validating function
            def create(self, validate_data):
                return Student.objects.create(**validate_data)




####  views / controller  : logic to handle incoming post request

          # function based view

          from django.shortcuts import render
          import io
          from rest_framework.parsers import JSONParser
          from .serializers import StudentSerializer
          from rest_framework.renderers import JSONRenderer
          from django.http import HttpResponse
          from django.views.decorators.csrf import csrf_exempt
          # disable crsf token
          # Create your views here.
          @csrf_exempt
          def student_create(request):
              if request.method == 'POST':
                  json_data = request.body
                  # converting from json to stream, then stream to python object 
                  stream = io.BytesIO(json_data)
                  pythondata = JSONParser().parse(stream)
                  serializer = StudentSerializer(data=pythondata)
                  if serializer.is_valid():
                      serializer.save()
                      res = {'msg':'data inserted'}
                      json_data = JSONRenderer().render(res)
                      return HttpResponse(json_data, content_type='application/json')
                  # if serializer is not valid
                  json_data = JSONRenderer().render(serializer.errors)
                  return HttpResponse(json_data, content_type='application/json')


#### root project urls : gs2/urls.py

        from django.contrib import admin
        from django.urls import path
        from api import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('stucreate/', views.student_create)
        ]



#### in postman 

        request type : post
        localhost:8000/stucreate/
        in body: 
        {
            "name":"ranjit",
            "roll":23,
            "city":"nammuru"
        }

#### result : check in admin UI : student table
