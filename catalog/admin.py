from django.contrib import admin

# Register your models here.

from .models import Author, Book, BookInstance, Language, Genre

@admin.register(Book)
class BookAdmin (admin.ModelAdmin):
    list_display=('title', 'summary', 'isbn', 'author', 'language', 'display_genre')
  
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
admin.site.register(Language)
admin.site.register(Genre)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]






