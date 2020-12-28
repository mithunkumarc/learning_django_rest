#### FieldLevelValidation : validating field inside serializers.py file


#### 1. create root project

        django-admin startproject fieldvalidationexample

#### 2. create application school

        cd fieldvalidationexample
        # create an app : school
        python manage.py startapp school


#### 3. add rest framework and school apps inside fieldvalidationexample/settings.py

        INSTALLED_APPS = [
          ...
            'rest_framework',
            'school',
        ]


#### 4. creating model : school/models.py


        from django.db import models

        # Create your models here.
        class Student(models.Model):
          name = models.CharField(max_length=100)
          roll = models.IntegerField()
          city = models.CharField(max_length=100)




#### 5. register in school/admin.py 

        from django.contrib import admin
        from .models import Student
        # Register your models here.
        @admin.register(Student)
        class StudentAdmin(admin.ModelAdmin):
          # display fields in admin UI
          list_display = ['id', 'name', 'roll', 'city']



#### 6. create and apply schema

        python manage.py makemigrations
        python manage.py migrate

        python manage.py createsuperuser
        admin 
        c0met123

        python manage.py runserver

#### 7. school/serializers.py : validation logic of roll number

        from rest_framework import serializers
        from .models import Student

        class StudentSerializer(serializers.Serializer):
            name = serializers.CharField(max_length=100)
            roll = serializers.IntegerField()
            city = serializers.CharField(max_length=100)

            # validating roll number
            def validate_roll(self, value):
                if value >= 200:
                    raise serializers.ValidationError('seat full')
                return value

            # for creating student
            def create(self, validated_data):
                return Student.objects.create(**validated_data)



#### 8. school/views.py : handle requests

        from django.shortcuts import render
        from rest_framework.response import Response
        from .models import Student
        from .serializers import StudentSerializer
        from rest_framework.decorators import api_view
        from django.views.decorators.csrf import csrf_exempt
        import io
        from rest_framework.parsers import JSONParser

        # get all students
        @api_view(['GET'])
        def studentList(request):
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)

        # create new student
        # @csrf_exempt
        @api_view(['POST'])
        def studentCreate(request):
            # convert incoming json to dictionary
            streamData = io.BytesIO(request.body)
            dictData = JSONParser().parse(streamData)
            serializer = StudentSerializer(data=dictData)
            if serializer.is_valid():
                serializer.save()
                return Response('created')
            else:
                return Response(serializer.errors)





#### 9. testing app : use postman : validation error may not seen in admin UI mode

        # read all students
        get : localhost:8000/studentlist
        response : list of student 

        # create student
        
        post : localhost:8000/studentcreate
        payload : 

         {
            "name": "manoj",
            "roll": 399,
            "city": "holalkere"
        }

        response error: 
        {
            "roll": [
                "seat full"
            ]
        }
        Note : you may not get error when you add student from admin UI
