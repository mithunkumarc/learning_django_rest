used to list all records , cannot read single record

views.py

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

urls.py

from django.contrib import admin
from django.urls import path
from school import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('studentapi', views.StudentList.as_view()),	# get request
        ]
          
          
