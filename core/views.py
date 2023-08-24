from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# this is the main endpoints to refer to
@api_view(['GET'])
def endpoints(request):
    data = ['books/', 'authors/', 'book/by/name/:name', 'author/by/name/:name']
    return Response(data)

# here we will add, delete, edit and get books
@api_view(['GET'])
def books_list(request):
    if request.method == 'GET':
        pass
