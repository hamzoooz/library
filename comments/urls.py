from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.comments , name='comments'),
    path('book/<slug:slug>/add_comment/', views.add_comment, name='add_comment'),
    # path('book/<slug:slug>/delete_comment/', views.delete_comment, name='delete_comment'),
    path('delete_comment/<int:pk>', views.delete_comment, name='delete_comment'),
]
