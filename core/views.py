from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.exceptions import NotFound
# Create your views here.

# this is the main endpoints to refer to
@api_view(['GET'])
def endpoints(request):
    data = ['books/', 'authors/', 'book/by/name/:name', 'author/by/name/:name']
    return Response(data)

# here we will add, delete, edit and get books
@api_view(['GET', 'POST'])
def books_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        name = data['name']
        description = data['description']
        publication_year = data['publication_year']
        
        book = Book.objects.create(name=name,
                                    description=description,
                                      publication_year=publication_year)
        for author in data['authors']:
            try:
                author = Author.objects.get(name=author)
                book.authors.add(author)
            except:
                raise NotFound()
            
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)
    
# here we will add, delete, edit and get authors
@api_view(['GET', 'POST'])
def authors_list(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        name = data['name']
        info = data['info']
   
        author = Author.objects.create(name=name, info=info)
        for book in data['books']:
            try:
                book = Book.objects.get(name=book)
                author.books.add(book)
            except:
                raise NotFound()
        serializer = AuthorSerializer(author, many=False)
        return Response(serializer.data)
        

