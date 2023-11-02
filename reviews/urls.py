from django.urls import path
from . import views

urlpatterns = [
    path('edit/<int:review_id>', views.edit_reviews, name='edit_reviews'),
]