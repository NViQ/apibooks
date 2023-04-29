import json
from django.urls import reverse
from rest_framework import status
from pytest_django.asserts import assertJSONEqual
from .conftest import user, author, book
from apilib.models import Books


def test_book_list_get(client, book):
    url = reverse('book_list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()['books']) == 1
    assertJSONEqual(json.dumps(response.json()['books'][0]), json.dumps({'id': book.id, 'title': book.title, 'author': {'id': book.author.id, 'first_name': book.author.first_name, 'last_name': book.author.last_name, 'birth_date': str(book.author.birth_date)}, 'description': book.description, 'publication_date': str(book.publication_date)}))


def test_book_list_post(client, user):
    url = reverse('book_list')
    data = {
        'title': 'Anna Karenina',
        'author': user.id,
        'description': 'Some descriptions',
        'publication_date': '1899-01-01'
    }
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['id'] == 2


def test_book_list_post_with_wrong_author(client, author):
    url = reverse('book_list')
    data = {
        'title': 'Anna Karenina',
        'author': author.id + 1,  # wrong author id
        'description': 'Some descriptions',
        'publication_date': '1999-01-01'
    }
    response = client.post(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'author' in response.json()


def test_book_detail_get(client, book):
    url = reverse('book_detail', kwargs={'pk': book.id})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assertJSONEqual(json.dumps(response.json()), json.dumps({'id': book.id, 'title': book.title, 'author': {'id': book.author.id, 'first_name': book.author.first_name, 'last_name': book.author.last_name, 'birth_date': str(book.author.birth_date)}, 'description': book.description, 'publication_date': str(book.publication_date)}))


def test_book_detail_put(client, book):
    url = reverse('book_detail', kwargs={'pk': book.id})
    data = {
        'title': 'New Title',
        'author':book.author.id,
        'description': 'A new description',
        'publication_date': '2001-11-11'
        }
    response = client.put(url, data)
    assert response.status_code == status.HTTP_200_OK
    book.refresh_from_db()
    assert book.title == 'New Title'
    assert book.description == 'A new description'
    assert str(book.publication_date) == '2001-11-11'

def test_book_detail_delete(client, book):
    url = reverse('book_detail', kwargs={'pk': book.id})
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Books.objects.filter(pk=book.id).exists() is False

def test_book_form_get(client, book):
    url = reverse('book_form', kwargs={'pk': book.id})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.context['book'] == book

def test_book_form_get_no_book(client):
    url = reverse('book_form')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.context['book'] is None

def test_book_form_post(client, user):
    url = reverse('book_form')
    data = {
    'title': 'War and Peace',
    'author': user.id,
    'description': 'Some descriptions',
    'publication_date': '1888-01-01'
    }
    response = client.post(url, data)
    assert response.status_code == status.HTTP_302_FOUND
    book = Books.objects.get(title='War and Peace')
    assert book.author == user
    assert str(book.publication_date) == '1888-01-01'
