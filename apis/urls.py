from django.urls import path
from . import views

urlpatterns = [
    path('api/books', views.list_books, name="list_book"),
    path('api/book/<int:pk>', views.book_detail_pk, name="list_book"),
    path('api/book/<str:slug>', views.book_detail_slug, name="list_book"),
    
    
]

