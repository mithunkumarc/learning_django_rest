from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request, pk=None):
	if request.method == 'GET':
		if pk is not None:
			stu = Student.objects.get(id=pk)
			serializer = StudentSerializer(stu)
			return Response(serializer.data)
		stu = Student.objects.all()
		serializer = StudentSerializer(stu, many=True)
		return Response(serializer.data)
	if request.method == 'POST':
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response('created')
		return Response(serializer.errors)
	if request.method == 'PUT':
		id = pk
		stu = Student.objects.get(pk = id)
		serializer = StudentSerializer(stu, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response('updated data')
		return Response(serializer.errors)

	if request.method == 'PATCH':
		id = pk
		stu = Student.objects.get(pk=id)
		serializer = StudentSerializer(stu, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response('partially updated data')
		return Response(serializer.errors)
    
	if request.method == 'DELETE':
		id = pk
		stu = Student.objects.get(pk=id)
		stu.delete()
		return Response('Deleted')
