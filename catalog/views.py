from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Catalog app is working! 🎉")
from django.views import generic

from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    num_genres = Genre.objects.filter(name__istartswith="a").count()
    books_english = Book.objects.filter(title__istartswith="h").count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres':num_genres,
        'books_english':books_english,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


# class based view
class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    queryset = Book.objects.filter(title__icontains='harry')[:5]
    template_name = 'django_local_library/catalog/templates/catalog/book_list.html'


# class books (generic.ListView):



