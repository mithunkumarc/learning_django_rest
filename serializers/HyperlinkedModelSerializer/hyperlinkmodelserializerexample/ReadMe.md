#### HyperlinkModelSerializer : provides new field url. hyperlink to current object detail

#### create root project

        django-admin startproject hyperlinkmodelserializerexample

#### create an app : album

        cd hyperlinkmodelserializerexample
        python manage.py startapp album

#### hyperlinkmodelserializerexample/settings.py

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

        class Song(models.Model):
          title = models.CharField(max_length=100)
          singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="song")
          duration = models.IntegerField()



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

        class SingerSerializer(serializers.HyperlinkedModelSerializer):
          class Meta:
            model = Singer
            fields = ['id', 'name', 'gender','url']     # url aviailable, hyperlink to current object

        class SongSerializer(serializers.HyperlinkedModelSerializer):
          class Meta:
            model = Song
            fields = ['id', 'title', 'duration','url']  # url aviailable, hyperlink to current object  


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
          
          
#### hyperlinkmodelserializerexample/urls.py

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




#### testing : postman : 

get : http://localhost:8000/song : song list


          [
              {
                  "id": 1,
                  "title": "madikeri manju",
                  "duration": 3,
                  "url": "http://localhost:8000/song/1/"      # new field url, hyperlink to current object detail
              },
              {
                  "id": 2,
                  "title": "car car",
                  "duration": 4,
                  "url": "http://localhost:8000/song/2/"
              },
              {
                  "id": 3,
                  "title": "yedetumbi",
                  "duration": 5,
                  "url": "http://localhost:8000/song/3/"
              },
              {
                  "id": 4,
                  "title": "hosa",
                  "duration": 4,
                  "url": "http://localhost:8000/song/4/"
              }
          ]

get : http://localhost:8000/singer

          [
              {
                  "id": 1,
                  "name": "subbanna",   
                  "gender": "male",
                  "url": "http://localhost:8000/singer/1/"      # new field url, hyperlink to current object detail
              },
              {
                  "id": 2,
                  "name": "jayashree",
                  "gender": "female",
                  "url": "http://localhost:8000/singer/2/"
              },
              {
                  "id": 3,
                  "name": "mysore anantswamy",
                  "gender": "male",
                  "url": "http://localhost:8000/singer/3/"
              }
          ]
