from django.urls import path

from archive import views
urlpatterns = [
  
    path('upload/',views.get_data, name="get_book"),

]

