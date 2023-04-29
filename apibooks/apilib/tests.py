from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apilib.models import Books
from pytest_django.asserts import assertContains, assertJSONEqual
from pytest import mark


from django.urls import reverse
from rest_framework import status


def test_book_list_get(client, django_db_setup):
    url = reverse('book_list')
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json().get('books')) == 0


def test_book_list_post(client, django_db_setup):
    url = reverse('book_list')
    data = {
        'title': 'Test Book',
        'author': 'Test Author',
        'published_date': '2022-05-01',
        'isbn': '1234567890'
    }
    response = client.post(url, data=data, content_type='application/json')

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json().get('title') == data['title']


def test_book_detail_get(client, django_db_setup):
    book = Book.objects.create(
        title='Test Book',
        author='Test Author',
        published_date='2022-05-01',
        isbn='1234567890'
    )
    url = reverse('book_detail', kwargs={'pk': book.pk})
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json().get('title') == book.title


def test_book_detail_put(client, django_db_setup):
    book = Books.objects.create(
        title='Test Book',
        author='Test Author',
        published_date='2022-05-01',
        isbn='1234567890'
    )
    url = reverse('book_detail', kwargs={'pk': book.pk})
    data = {
        'title': 'Updated Test Book',
        'author': 'Updated Test Author',
        'published_date': '2022-05-02',
        'isbn': '0987654321'
    }
    response = client.put(url, data=data, content_type='application/json')

    assert response.status_code == status.HTTP_200_OK
    assert response.json().get('title') == data['title']


def test_book_detail_delete(client, django_db_setup):
    book = Books.objects.create(
        title='Test Book',
        author='Test Author',
        published_date='2022-05-01',
        isbn='1234567890'
    )
    url = reverse('book_detail', kwargs={'pk': book.pk})
    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Books.objects.filter(pk=book.pk).exists() is False


def test_book_form_get(client, django_db_setup):
    url = reverse('book_form')
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK


def test_book_form_post(client, django_db_setup):
    url = reverse('book_form')
    data = {
        'title': 'Test Book',
        'author': 'Test Author',
        'published_date': '2022-05-01',
        'isbn': '1234567890'
    }
    response = client.post(url, data=data)

    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == reverse('book_detail', kwargs={'pk': 1})


def test_book_form_put(client, django_db_setup):
    book = Book.objects.create(
        title='Test Book',
        author='Test Author',
        published_date='2022-05-01',
        isbn='1234567890'
    )
    url = reverse('book_form', kwargs={'pk': book.pk})
data = {
'title': 'Updated Test Book',
'author': 'Updated Test Author',
'published_date': '2023-01-01',
'isbn': '0987654321'
}
response = client.put(url, data=data)
assert response.status_code == 302
assert response.url == reverse('book_detail', kwargs={'pk': book.pk})
updated_book = Book.objects.get(pk=book.pk)
assert updated_book.title == data['title']
assert updated_book.author == data['author']
assert str(updated_book.published_date) == data['published_date']
assert updated_book.isbn == data['isbn']