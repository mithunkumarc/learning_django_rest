#### foreign key example: link two tables
##### single artist : multiple album

#### this is example for manytoone relationship too


#### 1. create root project

        django-admin startproject foreignkeyexample
        cd foreignkeyexample

#### 2. create an app : song

        python manage.py startapp song

#### 3. foreignkeyexample/settings.py

        INSTALLED_APPS = [
          ...
            'rest_framework',
            'song',
        ]


#### song/models.py

        from django.db import models

        class Musician(models.Model):
            first_name = models.CharField(max_length=50)
            last_name = models.CharField(max_length=50)
            instrument = models.CharField(max_length=100)

        class Album(models.Model):
            artist = models.ForeignKey(Musician, on_delete=models.CASCADE)    # foreign key here: from views just sending id is enough
            name = models.CharField(max_length=100)
            release_date = models.DateField()
            num_stars = models.IntegerField()



#### register models in song/admin.py 

        from django.contrib import admin
        from .models import Musician, Album

        @admin.register(Musician)
        class MusicianAdmin(admin.ModelAdmin):
            # list all fields in table(Admin UI)
            # id : default field created by django
            list_display = ['id', 'first_name', 'last_name', 'instrument']


        @admin.register(Album)
        class AlbumAdmin(admin.ModelAdmin):
            # list all fields in table(Admin UI)
            # id : default field created by django
            list_display = ['id', 'artist', 'name', 'release_date', 'num_stars']


#### create schema and apply

        python manage.py makemigrations
        python manage.py migrate

#### create admin user

        python manage.py createsuperuser
        admin 
        c0met123

        to run server : python manage.py runserver


#### create song/serializers.py 

        from rest_framework import serializers
        from .models import Musician, Album

        class MusicianSerializer(serializers.ModelSerializer):
            class Meta:
                model = Musician    # name of the model serializing
                fields = '__all__' # may be requesting to serialize all fields


        class AlbumSerializer(serializers.ModelSerializer):
            class Meta:
                model = Album      # name of the model serializing 
                fields = '__all__' # may be requesting to serialize all fields



#### song/views.py : only selected operations : not full crud operations available


            from django.shortcuts import render
            from rest_framework.response import Response
            from .models import Album, Musician
            from .serializers import AlbumSerializer, MusicianSerializer
            from rest_framework.decorators import api_view
            from django.views.decorators.csrf import csrf_exempt
            import io
            from rest_framework.parsers import JSONParser
            
            
            # get all albums
            @api_view(['GET'])
            def albumList(request):
                albums = Album.objects.all()
                serializer = AlbumSerializer(albums, many=True)
                return Response(serializer.data)

            # get all musicians
            @api_view(['GET'])
            def musicianList(request):
                musicians = Musician.objects.all()
                serializer = MusicianSerializer(musicians, many=True)
                return Response(serializer.data)

            # create an album
            @api_view(['POST'])
            def albumCreate(request):
                # convert incoming json to dictionary
                streamData = io.BytesIO(request.body)
                dictData = JSONParser().parse(streamData)
                serializer = AlbumSerializer(data=dictData)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print('error while creating event', serializer.error_messages)
                return Response(serializer.data)


#### foreignkeyexample/urls.py

        from django.contrib import admin
        from django.urls import path
        from song import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('albums/', views.albumList),
            path('musicians/', views.musicianList),
            path('albumcreate/', views.albumCreate),
        ]

#### use admin UI to create some Musicians and Albums

#### testing 

        1. create two musicians from admin UI
        2. create an album from admin UI
        3. get : localhost:8000/albums
        4. get : localhost:8000/musicians

        

#### creating albums : postman

        request type : post
        localhost:8000/albumcreate/ # follow urls.py pattern, slash also important
        payload : make sure artist table has record with ID : 2
        same artist(musician id 2) has two albums "highway" and 'ranjhana'
        {
            "name": "highway",
            "release_date": "2020-12-01",
            "num_stars": 6,
            "artist": 2 
        }
         
        post : localhost:8000/albumcreate/
        payload : 
        {
            "name": "ranjhana",
            "release_date": "2020-12-01",
            "num_stars": 6,
            "artist": 2
        }
        
