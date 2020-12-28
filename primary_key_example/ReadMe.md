#### Automatic primary key : 

By default, Django gives each model the following field:


        id = models.AutoField(primary_key=True)

This is an auto-incrementing primary key.

If you’d like to specify a custom primary key, specify primary_key=True on one of your fields.   
If Django sees you’ve explicitly set Field.primary_key, it won’t add the automatic id column.  
Each model requires exactly one field to have primary_key=True (either explicitly declared or automatically added).  

## steps to implement example : duplicating primary key raises error

#### 1. create root project

                django-admin startproject primarykeyexample
                
#### 2. create an app : supermarket

                cd primarykeyexample
                python manage.py startapp supermarket

#### 3. primarykeyexample/settings.py

                INSTALLED_APPS = [
                        ...
                    'rest_framework',
                    'supermarket',
                ]


#### 4. supermarket/models.py

                from django.db import models

                class Fruit(models.Model):
                    name = models.CharField(max_length=100, primary_key=True)


#### register Fruit model in supermarket/admin.py 


                from django.contrib import admin
                from .models import Fruit
                # Register your models here.
                # admin.site.register(Fruit)

                @admin.register(Fruit)
                class FruitAdmin(admin.ModelAdmin):
                    # list all fields in table(Admin UI)
                    list_display = ['name']



#### create and apply db schema

                python manage.py makemigrations
                python manage.py migrate

                python manage.py createsuperuser
                admin 
                c0met123

                python manage.py runserver

#### in admin ui : try to add duplicate fruit : Fruit with this Name already exists.


#### create: serializers.py : class FruitSerializer

                from rest_framework import serializers
                from .models import Fruit

                class FruitSerializer(serializers.ModelSerializer):
                    class Meta:
                        model = Fruit
                        fields = '__all__' # may be requesting to serialize all fields




#### supermarket/views.py

                from django.shortcuts import render
                from rest_framework.response import Response
                from .models import Fruit
                from .serializers import FruitSerializer
                from rest_framework.decorators import api_view
                from django.views.decorators.csrf import csrf_exempt
                import io
                from rest_framework.parsers import JSONParser
                # Create your views here.
                # get all fruits
                @api_view(['GET'])
                def fruitList(request):
                    fruits = Fruit.objects.all()
                    serializer = FruitSerializer(fruits, many=True)
                    return Response(serializer.data)


                # create a fruit
                @api_view(['POST'])
                def fruitCreate(request):
                    # convert incoming json to dictionary
                    streamData = io.BytesIO(request.body)
                    dictData = JSONParser().parse(streamData)
                    serializer = FruitSerializer(data=dictData)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    else:
                        print('error while creating event', serializer.errors)
                        return Response(serializer.errors)




#### primarykeyexample/urls.py

                from django.contrib import admin
                from django.urls import path
                from supermarket import views

                urlpatterns = [
                    path('admin/', admin.site.urls),
                    path('fruits/', views.fruitList),
                    path('fruitcreate/', views.fruitCreate)
                ]


#### test example : use postman : try to enter duplicate fruit 

                localhost:8000/fruitcreate/ : post : run twice in postman
                {
                    "name": "banana"
                }

                response error :  
                "name": [
                        "fruit with this name already exists."
                    ]
