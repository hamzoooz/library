from django.urls import path
from . import views

urlpatterns = [
    path('my_library/add/', views.add_book , name='add_book'),
    path('my_library/edit_book/<int:pk>/', views.edit_book , name='edit_book'),
    path('my_library/delet_book/<int:pk>', views.delet_book, name='delet_book'),
    path('incres_number_of_download/<int:pk>',views.incres_number_of_download, name='incres_number_of_download'),
    
    
    path('', views.frontpage, name='frontpage'),
    path('book/<slug:slug>/', views.book_detail,name='book_detail'),
    path('categories/', views.category, name='categories'),
    path('category/<slug:slug>/', views.category_detail,name='category_detail'),
    
    # Pages 
    path('trending_page/', views.trending_page,name='trending_page'),
    path('recent_page/', views.recent_page,name='recent_page'),
    path('feed_page/', views.feed_page,name='feed_page'),
    path('random_books/', views.random_books,name='random_books'),
    
    path('test_template/', views.test_template,name='test_template'),
    
]

