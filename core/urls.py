from django.urls import path
from . import views
urlpatterns = [
    path('', views.endpoints, name='endpoints'),
    path('books/', views.books_list, name='books'),
    path('authors/', views.authors_list, name='authors'),
]
