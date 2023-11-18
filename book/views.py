from django.shortcuts import render

# Create your views here.

from .models import Book, Author, Review

from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)



class BookList(ListView):
    model = Book



class BookDetails(DetailView):
    model = Book



class CreateBook(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/home/'



class EditBook(UpdateView):
    model = Book
    fields = '__all__'
    success_url = '/home/'


class DeleteBook(DeleteView):
    model = Book
    success_url = '/home/'


# def home(request):
#     books = Book.objects.all()


#     context = {'book_list': books}

#     return render(request, 'book/book_list.html', context)


