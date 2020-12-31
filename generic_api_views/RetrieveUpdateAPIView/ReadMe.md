#### RetrieveUpdateAPIView : Used for read or update endpoints to represent a single model instance.

#### reads/update only one record : request type for reading is get, for update is put and patch. In urls id must be mentioned.


#### sample implementation : 

#### in your app : school/views.py

        from django.shortcuts import render
        # from rest_framework.response import Response
        from rest_framework.decorators import api_view
        from .models import Student
        from .serializers import StudentSerializer
        from rest_framework.views import APIView
        from rest_framework.generics import RetrieveUpdateAPIView

        class StudentRetrieveUpdate(RetrieveUpdateAPIView):
          queryset = Student.objects.all()
          serializer_class = StudentSerializer


#### in rootproject/urls.py

        from django.contrib import admin
        from django.urls import path
        from school import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            # supports post, patch and get(read single record)
            path('studentretrieveupdate/<int:pk>', views.StudentRetrieveUpdate.as_view()),	
        ]
