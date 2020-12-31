#### UpdateAPIView : update single instance/record at a time

#### support both put and patch requests

#### sample

#### in your app: school/views.py

        from django.shortcuts import render
        # from rest_framework.response import Response
        from rest_framework.decorators import api_view
        from .models import Student
        from .serializers import StudentSerializer
        from rest_framework.views import APIView
        from rest_framework.generics import UpdateAPIView

        class StudentUpdate(UpdateAPIView):
          queryset = Student.objects.all()
          serializer_class = StudentSerializer



#### rootproject/urls.py

        from django.contrib import admin
        from django.urls import path
        from school import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('studentupdateapi/<int:pk>', views.StudentUpdate.as_view()),	# put/patch : update record
        ]



