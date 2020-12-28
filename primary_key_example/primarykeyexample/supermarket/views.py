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
