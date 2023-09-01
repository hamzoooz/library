from django.urls import path
from chat import views
urlpatterns = [
    path('messages/', views.all_messages, name='all_messages' ),    
    path('send_message/<str:recever>', views.send_message , name='send_message'),
    path('get_message/<str:recever>', views.get_message, name='get_message'),
    path('messages/<str:pk>', views.view_messages, name='view_messages'),
]
