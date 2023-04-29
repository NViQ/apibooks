from django.contrib import admin
from .models import Authors, Books

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date')
    list_display_links = ('id', 'first_name')

class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'description', 'publication_date')
    list_display_links = ('id', 'title')


admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Books, BooksAdmin)
