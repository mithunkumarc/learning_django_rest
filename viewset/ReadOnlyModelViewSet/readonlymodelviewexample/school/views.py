from django.shortcuts import render
# from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

class StudentReadOnlyModelViewSet(ReadOnlyModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
