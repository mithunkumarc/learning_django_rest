from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

#by default api view accept only get requests : @api_view(['GET'])
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response("request type is GET : hello world")
    if request.method == 'POST':
        return Response("request type is POST : hello world")
