# from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('manage/', views.manage, name='manage'),
    path('manage/move_to_draft/<int:pk>', views.move_to_draft, name='move_to_draft' ),
    path('manage/move_to_delete/<int:pk>', views.move_to_delete, name='move_to_delete' ),
    path('manage/move_to_waiting/<int:pk>', views.move_to_waiting, name='move_to_waiting' ),
    path('manage/move_to_published/<int:pk>', views.move_to_published, name='move_to_published' ),
    path('manage/move_to_abrov/<int:pk>', views.move_to_abrov, name='move_to_abrov' ),
    path('manage/move_to_not_abrov/<int:pk>', views.move_to_not_abrov, name='move_to_not_abrov'),
]
