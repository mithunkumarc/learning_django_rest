#### RetrieveUpdateDestroyAPIView : read/update/delete : only single record. supported requests  put/patch/get/delete

        Used for read-write-delete endpoints to represent a single model instance.

        Provides get, put, patch and delete method handlers.

source : https://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdatedestroyapiview


#### in your app : school/views.py

        from django.shortcuts import render
        # from rest_framework.response import Response
        from rest_framework.decorators import api_view
        from .models import Student
        from .serializers import StudentSerializer
        from rest_framework.views import APIView
        from rest_framework.generics import RetrieveUpdateDestroyAPIView

        class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
          queryset = Student.objects.all()
          serializer_class = StudentSerializer



#### rootproject/urls.py

        from django.contrib import admin
        from django.urls import path
        from school import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            # supports get, delete, put ,patch : only for single record
            path('studentretrieveupdatedestroy/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),	
        ]
