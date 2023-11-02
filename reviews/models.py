from django.db import models

from profiles.models import UserProfile
from products.models import Product

class Review(models.Model):
    """ A model for users to review products """

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    body = models.TextField(max_length=1024)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.user} rated {self.product}'
