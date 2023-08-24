from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Book, Author

class AuthorSerializer(ModelSerializer):
    books = SerializerMethodField()
    class Meta:
        model = Author
        fields = '__all__'

    def get_books(self, obj):
        books = obj.books.all()
        return [book.name for book in books]


class BookSerializer(ModelSerializer):
    authors = SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_authors(self, obj):
        authors = obj.authors.all()
        return [author.name for author in authors]
