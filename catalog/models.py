from django.db import models
from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower

# Create your models here.
# genre model
class Genre(models.Model):

    name = models.CharField(max_length=200, unique=True,  help_text="Enter a Book Genre ex(fiction, romance, adventure, poetry, acedemic ) etc ...")


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('-genre-detail', args=[str(self.id)])
    

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = "Genre already exists (case insensitive match)"
            ),
        ]


class Language(models.Model):
    """Model representing the language in which the book was written"""
    name = models.CharField(max_length=30,unique=True, help_text="Enter the language in which the book is written ex(french, english, german, amharic, tigrigna, oromic, arabic)")
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('language detail', args=[str(self.id)])
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='language_name_case_insensitive_unique',
                violation_error_message = "Language already exists (case insensitive match)"
            ),
        ]

#genre model
class Book(models.Model):
    title = models.CharField(max_length=50, unique=True, help_text="Enter the Title of the book")
    author = models.ForeignKey("Author", on_delete = models.RESTRICT,  null=True )
    summary = models.TextField(max_length=1000, help_text="enter summary for the book ", unique=True)
    isbn = models.CharField('ISBN', max_length=13,
                            unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="select a genre for this book")

    language = models.ForeignKey(
        'Language', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.title
    
      
    def get_absolute_url(self):
        return reverse('-book-detail', args=[str(self.id)])
    

import uuid # Required for unique book instances

class BookInstance(models.Model):

    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'
    

 #author model
class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'



   
    

