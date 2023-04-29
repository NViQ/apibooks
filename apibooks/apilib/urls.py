from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
path('api/books/', views.book_list, name='book_list'),
path('api/books/int:pk/', views.book_detail, name='book_detail'),
path('api/books/create/', views.book_form, name='book_create'),
path('api/books/int:pk/update/', views.book_form, name='book_update'),
path('api/books/int:pk/delete/', views.book_detail, name='book_delete'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)