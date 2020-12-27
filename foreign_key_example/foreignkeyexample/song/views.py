from django.shortcuts import render
from rest_framework.response import Response
from .models import Album, Musician
from .serializers import AlbumSerializer, MusicianSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
# Create your views here.
# get all events
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
