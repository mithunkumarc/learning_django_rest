#### class based view crud : crud example using class based views : using class

#### put vs patch : 

        put : update all properties at the same time 
        patch: update selected properties 

#### create root project

        django-admin startproject classbasedcrudexample

#### create an app : school

        cd classbasedcrudexample
        python manage.py startapp school

#### classbasedcrudexample/settings.py

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
        from rest_framework.response import Response
        from rest_framework.decorators import api_view
        from .models import Student
        from .serializers import StudentSerializer
        from rest_framework.views import APIView

        class StudentAPI(APIView):
          def get(self, request, pk = None, format = None):
            # this is for reading single student record
            if pk is not None:
              stu = Student.objects.get(id = pk)
              serializer = StudentSerializer(stu)
              return Response(serializer.data)
            # this is for reading all student records
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many = True)
            return Response(serializer.data)

          def post(self, request, format = None):#pk skipped
            serializer = StudentSerializer(data = request.data)
            if serializer.is_valid():
              serializer.save()
              return Response('student created')
            return Response(serializer.errors)

          # pk : id of object being updated
          # put used to update all fields	
          def put(self, request, pk,format= None):
            id = pk
            stu = Student.objects.get(pk = id)
            # stu : old instance
            # request.data : new instance
            serializer = StudentSerializer(stu, data=request.data)
            if serializer.is_valid():
              serializer.save()
              msg = f"student with id {pk} updated"
              return Response(msg)
            else:
              return Response(serializer.errors)

          # patch: used to updated only specific fields/partial data
          # pk : id of object being updated partially		
          def patch(self, request, pk, format=None):
            id = pk
            # stu old instance
            stu = Student.objects.get(pk=id)
            # request.data : new instance
            serializer = StudentSerializer(stu, data=request.data, partial = True)
            if serializer.is_valid():
              serializer.save()
              msg = f'student with {pk} partially updated'
              return Response(msg)
            else:
              return Response(serializer.errors)

          def delete(self, request, pk, format=None):
            id = pk
            try:
              stu = Student.objects.get(pk=id)
              stu.delete()
            except:
              msg = f"student {pk} does not exist"
              return Response(msg)
            msg = f'student with id {pk} deleted'
            return Response(msg)


#### classbasedcrudexample/urls.py

            from django.contrib import admin
            from django.urls import path
            from school import views

            urlpatterns = [
                path('admin/', admin.site.urls),
                path('studentapi', views.StudentAPI.as_view()),	# handles post
                path('studentapi/<int:pk>', views.StudentAPI.as_view()),  # handle : get delete put patch
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
