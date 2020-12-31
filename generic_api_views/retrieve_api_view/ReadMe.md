RetrieveAPIView : used to read single instance 

#### usage

#### in your app  :school/views.py

        from django.shortcuts import render
        # from rest_framework.response import Response
        from rest_framework.decorators import api_view
        from .models import Student
        from .serializers import StudentSerializer
        from rest_framework.views import APIView
        from rest_framework.generics import RetrieveAPIView

        class StudentRetrieve(RetrieveAPIView):
          queryset = Student.objects.all()
          serializer_class = StudentSerializer


#### rootproject/urls/py

        from django.contrib import admin
        from django.urls import path
        from school import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('studentretrieveapi/<int:pk>', views.StudentRetrieve.as_view()),	# get : create record
        ]
