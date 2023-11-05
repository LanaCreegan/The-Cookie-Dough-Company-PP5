from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourites, name='favourites'),
    path('add_to_favourites/<int:product_id>/', views.add_to_favourites, name='add_to_favourites'),
    path('remove_from_favourites/<int:product_id>/', views.remove_from_favourites, name='remove_from_favourites'),
]