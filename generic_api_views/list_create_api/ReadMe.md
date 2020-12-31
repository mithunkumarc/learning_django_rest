ListCreateAPIView : reading list of all records and creating new record. supports get(list) and post(new record) request type.


#### sample example 

#### in app : school/views.py

        from django.shortcuts import render
        # from rest_framework.response import Response
        from rest_framework.decorators import api_view
        from .models import Student
        from .serializers import StudentSerializer
        from rest_framework.views import APIView
        from rest_framework.generics import ListCreateAPIView

        class StudentListCreate(ListCreateAPIView):
          queryset = Student.objects.all()
          serializer_class = StudentSerializer


#### in rootproject urls.py : rootproject/urls.py

        from django.contrib import admin
        from django.urls import path
        from school import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('studentlistcreate', views.StudentListCreate.as_view()),	# list: get, create: post
        ]
