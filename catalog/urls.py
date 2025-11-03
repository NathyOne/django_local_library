from . import views
from django.urls import include, path

urlpatterns =[
    path('', views.index, name='index'), 
    path('books/', views.BookListView.as_view(), name='books')
]

