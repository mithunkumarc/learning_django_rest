#### HyperlinkRelatedField : instead of showing primary key ids , hyperlink is shown

#### create root project

        django-admin startproject hyperlinkrelatedfieldexample

#### create an app : album

        cd hyperlinkrelatedfieldexample
        python manage.py startapp album

#### hyperlinkrelatedfieldexample/settings.py

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
          # optional for hyperlinkrelatedfield i guess
          def __str__(self):
            return self.name

        class Song(models.Model):
          title = models.CharField(max_length=100)
          singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="song")
          duration = models.IntegerField()
          # optional for hyperlinkrelatedfield i guess
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
          # instead of song primary key, its hyperlink is shown
          song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="song-detail")
          class Meta:
            model = Singer
            fields = ['id', 'name', 'gender', 'song']

        class SongSerializer(serializers.ModelSerializer):
          # instead of singer primary key, its hyperlink is shown
          singer = serializers.HyperlinkedRelatedField(read_only=True, view_name="singer-detail")
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



#### serializerrelationexample/urls.py

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

get : http://localhost:8000/singer : singers

          [
              {
                  "id": 1,
                  "name": "subbanna",
                  "gender": "male",
                  "song": [
                      "http://localhost:8000/song/1/"       # hyperlinks are shown
                  ]
              },
              {
                  "id": 2,
                  "name": "jayashree",
                  "gender": "female",
                  "song": [
                      "http://localhost:8000/song/2/",
                      "http://localhost:8000/song/4/"
                  ]
              },
              {
                  "id": 3,
                  "name": "mysore anantswamy",
                  "gender": "male",
                  "song": [
                      "http://localhost:8000/song/3/"
                  ]
              }
          ]
          
get : http://localhost:8000/song : list of songs



            [
                {
                    "id": 1,
                    "title": "madikeri manju",
                    "singer": "http://localhost:8000/singer/1/",
                    "duration": 3
                },
                {
                    "id": 2,
                    "title": "car car",
                    "singer": "http://localhost:8000/singer/2/",        # hyperlink shown instead of primary key
                    "duration": 4
                },
                {
                    "id": 3,
                    "title": "yedetumbi",
                    "singer": "http://localhost:8000/singer/3/",
                    "duration": 5
                },
                {
                    "id": 4,
                    "title": "hosa",
                    "singer": "http://localhost:8000/singer/2/",
                    "duration": 4
                }
            ]
