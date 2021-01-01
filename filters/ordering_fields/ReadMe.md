The OrderingFilter class supports simple query parameter controlled ordering of results.

#### 1. if you don't mention ordering_fields : ascending descending ordering works for all fields. name , city and roll
         
#### 2. ordering_fields = ['name'] # works only for name
         
#### 3. ordering_fields = ['name', 'city'] # works only for name and city

sample : 

        from django.shortcuts import render
        from rest_framework.response import Response
        from rest_framework.decorators import api_view
        from .models import Student
        from .serializers import StudentSerializer
        from rest_framework.views import APIView
        from rest_framework.generics import ListAPIView
        from rest_framework import filters

        class StudentList(ListAPIView):
          queryset = Student.objects.all()
          serializer_class = StudentSerializer
          filter_backends = [filters.OrderingFilter]
          # if you don't mention ordering_fields : ascending descending ordering works for all fields
          ordering_fields = ['name'] # works only for name
          # ordering_fields = ['name', 'city']
