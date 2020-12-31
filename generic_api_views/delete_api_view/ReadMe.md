# DestroyAPIView : delete single record : 
# folder was supposed tobe destroy_api_view

#### sample : in your app : school/views.py

        from django.shortcuts import render
        # from rest_framework.response import Response
        from rest_framework.decorators import api_view
        from .models import Student
        from .serializers import StudentSerializer
        from rest_framework.views import APIView
        from rest_framework.generics import DestroyAPIView

        class StudentDelete(DestroyAPIView):
          queryset = Student.objects.all()
          serializer_class = StudentSerializer


#### rootproject/urls.py

        from django.contrib import admin
        from django.urls import path
        from school import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('studentdeleteapi/<int:pk>', views.StudentDelete.as_view()),	# delete : delete record
        ]
