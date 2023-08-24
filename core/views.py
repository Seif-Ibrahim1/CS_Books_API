from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def endpoints(self):
    data = ['books/', 'authors/', 'book/by/name/:name', 'author/by/name/:name']
    return Response(data)
