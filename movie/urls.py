from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='movie-home'),
    path('search/', views.search, name='movie-search'),
    path('search/<str:query>/', views.search, name='movie-search')
]
