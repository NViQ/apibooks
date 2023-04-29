import pytest
from django.contrib.auth.models import User
from apilib.models import Authors, Books


@pytest.fixture
def user():
    return User.objects.create(username='testuser')


@pytest.fixture
def author():
    return Authors.objects.create(first_name='Leo', last_name='Tolstoy', birth_date='1828-09-09')


@pytest.fixture
def book(author):
    return Books.objects.create(title='War and Peace', author=author, description='A novel by Leo Tolstoy', publication_date='1869-01-01')