from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Books
from .forms import BookForm

@csrf_exempt
def book_list(request):

    #Отображает список всех книг.

    if request.method == 'GET':
        books = Books.objects.all()
        books_json = list(books.values())
        return JsonResponse({'books': books_json}, safe=False)

    elif request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            book_json = model_to_dict(book)
            return JsonResponse(book_json, status=201)
        else:
            return JsonResponse(form.errors, status=400)


@csrf_exempt
def book_detail(request, pk):

    #Отображает информацию о книге и позволяет обновить или удалить ее

    book = get_object_or_404(Books, pk=pk)

    if request.method == 'GET':
        book_json = model_to_dict(book)
        return JsonResponse(book_json)

    elif request.method == 'PUT':
        form = BookForm(request.PUT, instance=book)
        if form.is_valid():
            form.save()
            book_json = model_to_dict(book)
            return JsonResponse(book_json)
        else:
            return JsonResponse(form.errors, status=400)

    elif request.method == 'DELETE':
        book.delete()
        return JsonResponse({'message': 'Книга успешно удалена!'}, status=204)


def book_form(request, pk=None):

    #Отображает форму для добавления/обновления книги

    if pk:
        book = get_object_or_404(Books, pk=pk)
    else:
        book = None

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)

    return render(request, 'book_form.html', {'form': form, 'book': book})