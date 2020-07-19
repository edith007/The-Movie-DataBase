from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='movie-home'),
    path('show/', views.show, name='movie-show'),
    path('show/<int:showid>/', views.show, name='movie-show'),
    path('list/', views.showlist, name='movie-showlist'),
    path('list/<str:username>/', views.showlist, name='movie-showlist'),
    path('search/', views.search, name='movie-search'),
    path('search/<str:query>/', views.search, name='movie-search')
]
