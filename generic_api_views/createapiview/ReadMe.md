CreatApiView : used to create record : accept post request

syntax : 

#### in your app : school/views.py

        from django.shortcuts import render
        from rest_framework.response import Response
        from rest_framework.decorators import api_view
        from .models import Student
        from .serializers import StudentSerializer
        from rest_framework.views import APIView
        from rest_framework.generics import CreateAPIView

        class StudentCreate(CreateAPIView):
          queryset = Student.objects.all()
          serializer_class = StudentSerializer

#### configuer urls : rootproject/urls.py

          from django.contrib import admin
          from django.urls import path
          from school import views

          urlpatterns = [
              path('admin/', admin.site.urls),
              path('studentcreateapi', views.StudentCreate.as_view()),	# post : create record
              #path('studentapi/<int:pk>', views.StudentAPI.as_view()),  # handle : get delete put patch
          ]


