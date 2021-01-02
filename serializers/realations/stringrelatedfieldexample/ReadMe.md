#### without relations, linked fields are shown as primary key ids.

#### using StringRelatedField we can show string insteas of primary key ids. it is more readable. Note : (override __str__ method in model) class

#### serializer relations

#### create root project

        django-admin startproject stringrelatedfieldexample

#### create an app : album

        cd stringrelatedfieldexample
        python manage.py startapp album

#### stringrelatedfieldexample/settings.py

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
            return self.name  # choose your field to disply in linked field insted of primary key

        class Song(models.Model):
          title = models.CharField(max_length=100)
          singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="song")
          duration = models.IntegerField()
          def __str__(self):
            return self.title   # # choose your field to disply in linked field insted of primary key



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
          # make sure you have overridden Song class __str__ method
          song = serializers.StringRelatedField(many=True, read_only=True)
          class Meta:
            model = Singer
            fields = ['id', 'name', 'gender', 'song']

        class SongSerializer(serializers.ModelSerializer):
          # make sure you have overridden Singer class __str__ method
          singer = serializers.StringRelatedField(read_only=True)
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



#### stringrelatedfieldexample/urls.py

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


get : song : http://localhost:8000/song

              [
                  {
                      "id": 1,
                      "title": "madikeri manju",
                      "singer": "subbanna",       # instead of id, string is being shown, name of singer
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


get  :singer : http://localhost:8000/singer

          [
              {
                  "id": 1,
                  "name": "subbanna",
                  "gender": "male",
                  "song": [
                      "madikeri manju"          # song name is shown instead of song id.
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


