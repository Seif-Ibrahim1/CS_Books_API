from django.urls import path
from . import views
urlpatterns = [
    path('', views.endpoints, name='endpoints'),
    path('v1/books/', views.books_list, name='books'),
    path('v1/authors/', views.authors_list, name='authors'),
    path('v1/books/<int:pk>', views.book_by_id, name='book_by_name'),
    path('v1/authors/<int:pk>', views.author_by_id, name='author_by_name'),
]
