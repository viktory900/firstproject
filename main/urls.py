from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('comedy/', views.comedy, name='comedy'),
    path('drama/', views.drama, name='drama'),
    path('horror/', views.horror, name='horror'),

    path('main/', views.main_page, name='main_page'), 
    path('main/toggle-theme/', views.toggle_theme, name='toggle_theme'), 
]
