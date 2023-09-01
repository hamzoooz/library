from django.urls import path
from . import views

urlpatterns = [
    path('qoutes/', views.qoutes, name='qoutes'),
    # path('add_quote', views.add_quote, name='add_quote'),
    path('book/<slug:slug>/add_quote/', views.add_quote, name='add_quote'),
    path('delete_quote/<int:pk>', views.delete_quote, name='delete_quote'),
]

