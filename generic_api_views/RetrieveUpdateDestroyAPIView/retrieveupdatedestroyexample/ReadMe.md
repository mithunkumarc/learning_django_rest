#### retrieveupdatedestroy : read/update/delete single record: supported request types : get/put/patch/delete#### class based view crud : crud example using class based views : using class

#### put vs patch : 

        put : update all properties at the same time 
        patch: update selected properties 

#### create root project

        django-admin startproject retrieveupdatedestroyexample

#### create an app : school

        cd retrieveupdatedestroyexample
        python manage.py startapp school

#### retrieveupdatedestroyexample/settings.py

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
        from rest_framework.generics import RetrieveUpdateDestroyAPIView

        class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
          queryset = Student.objects.all()
          serializer_class = StudentSerializer


#### retrieveupdatedestroyexample/urls.py

        from django.contrib import admin
        from django.urls import path
        from school import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            # supports get, delete, put ,patch : only for single record
            path('studentretrieveupdatedestroy/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),	
        ]




#### testing : postman : 

1.read all studentds
 
       get : localhost:8000/studentapi 

2.read single student : 

        get : localhost:8000/studentapi/2

3. create student 

        post : localhost:8000/studentapi
        payload : 
        {
            "name": "bridjet",
            "roll": 22,
            "city": "secondcity"
        }

4. update fields

        PUT : localhost:8000/studentapi/2
        {
            "id": 2,
            "name": "bridjet jones",
            "roll": 23,
            "city": "new second city"
        }

5. update only name 

        PATCH : localhost:8000/studentapi/2
        payload : 
        {
            "name": "bridjet jonas"
        }
        response : "partially updated data"


6. delete 

        DELETE : localhost:8000/studentapi/1
        response : "Deleted"
