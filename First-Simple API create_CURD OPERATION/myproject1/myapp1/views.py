
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.views  import APIView
from rest_framework.decorators import api_view
# Create your class views here.
class MyclassView(APIView):
    def get(self, request, format=None):
        message={
            'Response':200,
            'Message':"Hello World!"
        }
        return Response(message)


#function based view

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})
