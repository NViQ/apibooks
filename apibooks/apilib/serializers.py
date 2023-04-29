from rest_framework import serializers
from .models import Authors, Books

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['id', 'first_name', 'last_name', 'birth_date']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'description', 'publication_date']
