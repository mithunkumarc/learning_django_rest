from django.shortcuts import render
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
# Create your views here.
# get all events
@api_view(['GET'])
def eventList(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

# get single event
@api_view(['GET'])
def eventDetail(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)

# create new event
# @csrf_exempt
@api_view(['POST'])
def eventCreate(request):
    # convert incoming json to dictionary
    streamData = io.BytesIO(request.body)
    dictData = JSONParser().parse(streamData)
    serializer = EventSerializer(data=dictData)
    if serializer.is_valid():
        serializer.save()
    else:
        print('error while creating event', serializer.error_messages)
    return Response(serializer.data)


# update
@api_view(['PUT'])
def eventUpdate(request, pk):
    event = Event.objects.get(id=pk)
    # read tobe update data sent by user
    streamData = io.BytesIO(request.body)
    dictData = JSONParser().parse(streamData)
    # instance : existing object data
    # data : tobe updated data
    serializer = EventSerializer(instance=event, data=dictData)
    if serializer.is_valid():
        serializer.save()
    else:
        print('error while creating event', serializer.error_messages)
    return Response(serializer.data)


#delete user :
@api_view(['DELETE'])
def eventDelete(request, pk):
    event = Event.objects.get(id=pk)
    if event:
        event.delete()
        return Response('deleted')
    else:
        return Response('error while deleting id : ',pk)
