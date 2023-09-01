from django.urls import path
from . import views
urlpatterns = [
    path('get_carusel', views.get_carusel , name="get_carusel"),
]
