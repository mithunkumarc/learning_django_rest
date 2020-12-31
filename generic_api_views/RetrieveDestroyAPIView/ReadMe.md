#### RetrieveDestroyAPIView : retrieve or destroy instance

#### Used for read or delete endpoints to represent a single model instance.

reference : https://www.django-rest-framework.org/api-guide/generic-views/#retrievedestroyapiview


#### in your app school/views.py

          from django.shortcuts import render
          # from rest_framework.response import Response
          from rest_framework.decorators import api_view
          from .models import Student
          from .serializers import StudentSerializer
          from rest_framework.views import APIView
          from rest_framework.generics import RetrieveDestroyAPIView

          class StudentRetrieveDestroy(RetrieveDestroyAPIView):
            queryset = Student.objects.all()
            serializer_class = StudentSerializer


#### in rootproject/urls.py

          from django.contrib import admin
          from django.urls import path
          from school import views

          urlpatterns = [
              path('admin/', admin.site.urls),
              # supports get(read single record) and delete(delete single record)
              path('studentretrievedestroy/<int:pk>', views.StudentRetrieveDestroy.as_view()),	
          ]
