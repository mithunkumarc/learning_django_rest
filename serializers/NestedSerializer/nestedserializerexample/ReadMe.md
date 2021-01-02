#### NestedSerializer: related object is completely shown instead of showing primary key

#### create root project

        django-admin startproject nestedserializerexample

#### create an app : album

        cd nestedserializerexample
        python manage.py startapp album

#### nestedserializerexample/settings.py

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
          # related name : sung is being used in SingerSerializer
          singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="sung")
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


        class SongSerializer(serializers.ModelSerializer):
          class Meta:
            model = Song
            fields = ['id', 'title', 'singer', 'duration']


        class SingerSerializer(serializers.ModelSerializer):
          sung = SongSerializer(many=True, read_only=True)
          class Meta:
            model = Singer
            fields = ['id', 'name', 'gender', 'sung']



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

#### nestedserializerexample/urls.py


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
                    "sung": [             # sung by subbanaa
                        {
                            "id": 1,
                            "title": "madikeri manju",
                            "singer": 1,
                            "duration": 3
                        }
                    ]
                },
                {
                    "id": 2,
                    "name": "jayashree",
                    "gender": "female",
                    "sung": [
                        {
                            "id": 2,
                            "title": "car car",
                            "singer": 2,
                            "duration": 4
                        },
                        {
                            "id": 4,
                            "title": "hosa",
                            "singer": 2,
                            "duration": 4
                        }
                    ]
                },
                {
                    "id": 3,
                    "name": "mysore anantswamy",
                    "gender": "male",
                    "sung": [
                        {
                            "id": 3,
                            "title": "yedetumbi",
                            "singer": 3,
                            "duration": 5
                        }
                    ]
                }
            ]

