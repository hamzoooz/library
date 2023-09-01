from django.urls import path
from . import views 
urlpatterns = [
    path('users/<str:username>/follow', views.follow, name='follow'),
    # path('book/<str:slug>/rating', views.rating_book, name='rating_book'),

    # # # path('rating', views.rating_system, name='rating_system'),
    # path('users/<str:username>/rating', views.rating_user, name='rating_user'),

]