from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

#by default api view accept only get requests : @api_view(['GET'])
@api_view()
def hello_world(request):
	return Response("hello world")
