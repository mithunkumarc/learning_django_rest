#### example : if serializers are not linked each other and models are having relationship. (many to one in this example)

#### many songs linked to single singer

if one model is related to another model, linked field displayed withrespect to foreign key ids  

example : singers sung songs. songs information shows as ids. 

          [
              {
                  "id": 1,
                  "name": "subbanna",
                  "gender": "male",
                  "song": [
                      1
                  ]
              },
              {
                  "id": 2,
                  "name": "jayashree",
                  "gender": "female",
                  "song": [
                      2,
                      4
                  ]
              },
              {
                  "id": 3,
                  "name": "mysore anantswamy",
                  "gender": "male",
                  "song": [
                      3
                  ]
              }
          ]
          
          
#### withoutrelationexample:  create root project

        django-admin startproject withoutrelationexample

#### create an app : album

        cd withoutrelationexample
        python manage.py startapp album

#### withoutrelationexample/settings.py

        INSTALLED_APPS = [
          ...
            'rest_framework',
            'album',
        ]


#### creating model : album/models.py


        from django.db import models

        # Create your models here.
        class Singer(models.Model):
          name = models.CharField(max_length=100)
          gender = models.CharField(max_length=100)
          def __str__(self):
            return self.name

        class Song(models.Model):
          title = models.CharField(max_length=100)
          singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="song")
          duration = models.IntegerField()
          def __str__(self):
            return self.title




#### register in album/admin.py 


        from django.contrib import admin
        from .models import Singer, Song
        # Register your models here.

        @admin.register(Singer)
        class SingerAdmin(admin.ModelAdmin):
          # display below fields in admin UI
          list_display = ['id', 'name', 'gender']


        @admin.register(Song)
        class SongAdmin(admin.ModelAdmin):
          # display below fields in admin UI
          list_display = ['id', 'title', 'singer', 'duration']


### create and apply schema

        python manage.py makemigrations
        python manage.py migrate

#### creating admin user

        python manage.py createsuperuser
        admin 
        c0met123

#### runserver

        python manage.py runserver

#### album/serializers.py

        from .models import Singer, Song
        from rest_framework import serializers

        class SingerSerializer(serializers.ModelSerializer):
          #song = serializers.StringRelatedField(many=True, read_only=True)
          class Meta:
            model = Singer
            fields = ['id', 'name', 'gender', 'song']

        class SongSerializer(serializers.ModelSerializer):
          class Meta:
            model = Song
            fields = ['id', 'title', 'singer', 'duration']




#### album/views.py

        from django.shortcuts import render
        from .serializers import SingerSerializer, SongSerializer
        from rest_framework import viewsets
        from .models import Singer, Song

        # Create your views here.
        class SingerViewSet(viewsets.ModelViewSet):
          queryset = Singer.objects.all()
          serializer_class = SingerSerializer

        class SongViewSet(viewsets.ModelViewSet):
          queryset = Song.objects.all()
          serializer_class = SongSerializer


#### withoutrelationexample/urls.py

from django.contrib import admin
from django.urls import path, include
from album import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('singer', views.SingerViewSet, basename='singer')
router.register('song', views.SongViewSet, basename='song')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]



#### testing : postman : many songs sung by a singer


        get: http://localhost:8000/singer


        [
            {
                "id": 1,
                "name": "subbanna",
                "gender": "male",
                "song": [
                    1           # ids are shown
                ]
            },
            {
                "id": 2,
                "name": "jayashree",
                "gender": "female",
                "song": [
                    2,
                    4
                ]
            },
            {
                "id": 3,
                "name": "mysore anantswamy",
                "gender": "male",
                "song": [
                    3
                ]
            }
        ]
