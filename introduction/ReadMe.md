#### Example : student list

#### requirement dependecies: use pip to install
	
      python 
      django web framework 
      django rest framework 
      virtual env is optional

#### creating root project "gs1" and app "api"

        > django-admin startproject gs1
        > cd gs1
        > python manage.py startapp api

#### add rest_framework app to project

      > settings.py : installed apps  

        # add below two lines
        rest_framework
        api
        
#### creating model(schema/entity for db)

        inside app api : 
        goto models.py

        from django.db import models

        # Create your models here.
        class Student(models.Model):
          name = models.CharField(max_length=100)
          roll = models.IntegerField()
          city = models.CharField(max_length=100)

#### create database

        # create schema
        >python manage.py makemigrations 
        # apply schema
        >python manage.py migrate
        # create admin
        >python manage.py createsuperuser
        #follow instructions create admin
        >python manage.py runserver

#### register Student model to admin 

        api/admin.py

        from django.contrib import admin
        from .models import Student
        # Register your models here.
        @admin.register(Student)
        class StudentAdmin(admin.ModelAdmin):
          list_disply = ['id', 'name', 'roll', 'city']

#### create student records

        > localhost:8000/admin 
        > you can see student link available in admin page

        > create three records and logout: now we try to access these records as rest service


#### db records read as json using serializers: create api/serializers.py file

        from rest_framework import serializers

        class StudentSerializer(serializers.Serializer):
            name = serializers.CharField(max_length=100)
            roll = serializers.IntegerField()
            city = serializers.CharField(max_length=100)


####  creating views (like controller in spring)

          #views.py

          from django.shortcuts import render
          from .models import Student
          from .serializers import StudentSerializer
          from rest_framework.renderers import JSONRenderer
          from django.http import HttpResponse
          # Create your views here.
          def student_detail(request):
              stu = Student.objects.get(id = 2)
              serializer = StudentSerializer(stu)
              json_data = JSONRenderer().render(serializer.data)
              return HttpResponse(json_data, content_type='application/json')


#### configuring urls.py:  root project urls 

          gs1/urls.py
          from django.contrib import admin
          from django.urls import path
          from api import views

          urlpatterns = [
              path('admin/', admin.site.urls),
              path('stuinfo/', views.student_detail),
          ]


#### test : reads only one student id:2
    
          browser> localhost:8000/stuinfo

### get student using request parameter : stuinfo/<id as req-parameter>

          url with request parameter
          for : localhost:8000/stuinfo/1


#### api/views.py

        from django.shortcuts import render
        from .models import Student
        from .serializers import StudentSerializer
        from rest_framework.renderers import JSONRenderer
        from django.http import HttpResponse
        # Create your views here.
        def student_detail(request, reqID):
            stu = Student.objects.get(id = reqID)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
	
#### configure root project : gs1/urls : 

        from django.contrib import admin
        from django.urls import path
        from api import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('stuinfo/<int:reqID>', views.student_detail),
        ]
	
	
### to read all students using localhost:8000/stuinfo


#### views.py : 

        from django.shortcuts import render
        from .models import Student
        from .serializers import StudentSerializer
        from rest_framework.renderers import JSONRenderer
        from django.http import HttpResponse
        # Create your views here.
        def student_detail(request, reqID):
            stu = Student.objects.get(id = reqID)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')


        # get all students
        def student_list(request):
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many = True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
	
	
#### gs1/urls.py

        from django.contrib import admin
        from django.urls import path
        from api import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('stuinfo/<int:reqID>', views.student_detail),
            path('stuinfo/', views.student_list), # returns all students
        ]


