from django.urls import path
from . import views

urlpatterns = [
    
    path('book/<str:slug>/rating', views.rating_book, name='rating_book'),
    # path('users/<int:pk>/rating/', views.rating_user, name='rating_user'),
    path('users/<str:user>/rating', views.rating_user, name='rating_user'),
    # path('users/<str:username>/rating', views.rating_user, name='rating_user'),
    
]
