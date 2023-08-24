from rest_framework.serializers import ModelSerializer
from .models import Book, Author
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


