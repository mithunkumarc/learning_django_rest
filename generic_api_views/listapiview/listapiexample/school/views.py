from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

class StudentList(ListAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

# class StudentAPI(APIView):
# 	def get(self, request, pk = None, format = None):
# 		# this is for reading single student record
# 		if pk is not None:
# 			stu = Student.objects.get(id = pk)
# 			serializer = StudentSerializer(stu)
# 			return Response(serializer.data)
# 		# this is for reading all student records
# 		stu = Student.objects.all()
# 		serializer = StudentSerializer(stu, many = True)
# 		return Response(serializer.data)

# 	def post(self, request, format = None):#pk skipped
# 		serializer = StudentSerializer(data = request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response('student created')
# 		return Response(serializer.errors)

# 	# pk : id of object being updated
# 	# put used to update all fields	
# 	def put(self, request, pk,format= None):
# 		id = pk
# 		stu = Student.objects.get(pk = id)
# 		# stu : old instance
# 		# request.data : new instance
# 		serializer = StudentSerializer(stu, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			msg = f"student with id {pk} updated"
# 			return Response(msg)
# 		else:
# 			return Response(serializer.errors)

# 	# patch: used to updated only specific fields/partial data
# 	# pk : id of object being updated partially		
# 	def patch(self, request, pk, format=None):
# 		id = pk
# 		# stu old instance
# 		stu = Student.objects.get(pk=id)
# 		# request.data : new instance
# 		serializer = StudentSerializer(stu, data=request.data, partial = True)
# 		if serializer.is_valid():
# 			serializer.save()
# 			msg = f'student with {pk} partially updated'
# 			return Response(msg)
# 		else:
# 			return Response(serializer.errors)

# 	def delete(self, request, pk, format=None):
# 		id = pk
# 		try:
# 			stu = Student.objects.get(pk=id)
# 			stu.delete()
# 		except:
# 			msg = f"student {pk} does not exist"
# 			return Response(msg)
# 		msg = f'student with id {pk} deleted'
# 		return Response(msg)
