from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.exceptions import NotFound
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# this is the main endpoints to refer to
@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def endpoints(request):
    data = ['v1/books/', 'v1/authors/', 'v1/books/:id', 'v1/authors/:id']
    return Response(data)

# here we will add, delete, edit and get books
@api_view(['GET', 'POST'])
def books_list(request):
    # /books/?query=
    if request.method == 'GET':
        query = request.GET.get('query')
        if(query == None):
            query = '' 
        books = Book.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        title = data['title']
        description = data['description']
        publication_year = data['publication_year']
        thumbnail_url = data['thumbnail_url']
        
        book = Book.objects.create(title=title,
                                    description=description,
                                      publication_year=publication_year,
                                      thumbnail_url=thumbnail_url)
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
        query = request.GET.get('query')
        if(query == None):
            query = ''
        authors = Author.objects.filter(Q(name__icontains=query))
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        name = data['name']
   
        author = Author.objects.create(name=name)
        for book in data['books']:
            try:
                book = Book.objects.get(title=book)
                author.books.add(book)
            except:
                raise NotFound()
        serializer = AuthorSerializer(author, many=False)
        return Response(serializer.data)
        

@api_view(['GET', 'PUT', 'DELETE'])
def book_by_id(request, pk):
    if request.method == 'GET':
        book = Book.objects.filter(id=pk)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)
    
    if request.method =='PUT':
        book = Book.objects.get(id=pk)
        data = request.data
        if 'title' in data:
            book.title = data['title']

        if 'description' in data:
            book.description = data['description']

        if 'publication_year' in data:
            book.publication_year = data['publication_year']

        if 'thumbnail_url' in data:
            book.thumbnail_url = data['thumbnail_url']

        if 'authors' in data:
            for author in data['authors']:
                try:
                    author = Author.objects.get(name=author)
                    book.authors.add(author)
                except:
                    raise NotFound()
        
        serializer = BookSerializer(book, many=False)
        book.save()
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        book = Book.objects.get(id=pk)
        book.delete()
        return Response('Deleted Succesfully')
    
@api_view(['GET', 'PUT', 'DELETE'])
def author_by_id(request, pk):
    if request.method == 'GET':
        author = Author.objects.filter(id=pk)
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)

    if request.method == 'PUT':
        author = Author.objects.get(id=pk)
        data = request.data

        if 'name' in data:
            author.name = data['name']

        if 'books' in data:
            for book in data['books']:
                try:
                    book = Book.objects.get(title=book)
                    author.books.add(book)
                except:
                    raise NotFound()
                
        serializer = AuthorSerializer(author, many=False)
        author.save()
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        author = Author.objects.get(id=pk)
        author.delete()
        return Response('Deleted Succesfully')