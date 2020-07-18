from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='movie-home'),
    path('show/', views.show, name='movie-show'),
    path('show/<int:showid>/', views.show, name='movie-show'),
    path('search/', views.search, name='movie-search'),
    path('search/<str:query>/', views.search, name='movie-search')
]
