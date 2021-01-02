#### SlugRelatedField

      instead of showing primary key of linked table, another field is chosen to shown. this field is called as slug field.
      ex : singer table choses title of song to dispay in its table instead of primary key
      this example is similar to StringRelatedField example
      SlugRelatedField may be used to represent the target of the relationship using a field on the target.
          

#### create root project

        django-admin startproject slugrelatedfieldexample

#### create an app : album

        cd slugrelatedfieldexample
        python manage.py startapp album

#### slugrelatedfieldexample/settings.py

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


        class SingerSerializer(serializers.ModelSerializer):
          # instead of showing primary key, title of song is shown. title becomes slug field	
          song = serializers.SlugRelatedField(many=True, read_only=True, slug_field="title")
          class Meta:
            model = Singer
            fields = ['id', 'name', 'gender', 'song']

        class SongSerializer(serializers.ModelSerializer):
          # instead of showing primary key, name of singer shown. name becomes slug field
          singer = serializers.SlugRelatedField(read_only=True, slug_field="name")
          class Meta:
            model = Song
            fields = ['id', 'title', 'singer', 'duration', 'singer']


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


#### slugrelatedfieldexample/urls.py


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


get : http://localhost:8000/singer  ; singerlist

          [
              {
                  "id": 1,
                  "name": "subbanna",
                  "gender": "male",
                  "song": [
                      "madikeri manju"      # title of song is chosen as slug field. instead of showing primary key
                  ]
              },
              {
                  "id": 2,
                  "name": "jayashree",
                  "gender": "female",
                  "song": [
                      "car car",
                      "hosa"
                  ]
              },
              {
                  "id": 3,
                  "name": "mysore anantswamy",
                  "gender": "male",
                  "song": [
                      "yedetumbi"
                  ]
              }
          ]


get : http://localhost:8000/song : list of songs


        [
            {
                "id": 1,
                "title": "madikeri manju",
                "singer": "subbanna",         # name of singer is shown(slug field) instead of primary key
                "duration": 3
            },
            {
                "id": 2,
                "title": "car car",
                "singer": "jayashree",
                "duration": 4
            },
            {
                "id": 3,
                "title": "yedetumbi",
                "singer": "mysore anantswamy",
                "duration": 5
            },
            {
                "id": 4,
                "title": "hosa",
                "singer": "jayashree",
                "duration": 4
            }
        ]
