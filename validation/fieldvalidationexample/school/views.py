from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

# get all students
@api_view(['GET'])
def studentList(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

# create new student
# @csrf_exempt
@api_view(['POST'])
def studentCreate(request):
    # convert incoming json to dictionary
    streamData = io.BytesIO(request.body)
    dictData = JSONParser().parse(streamData)
    serializer = StudentSerializer(data=dictData)
    if serializer.is_valid():
        serializer.save()
        return Response('created')
    else:
        return Response(serializer.errors)
