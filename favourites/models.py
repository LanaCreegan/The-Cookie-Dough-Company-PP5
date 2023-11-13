from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Favourites(models.Model):
    """
    Model to show all product items within the users favourites
    """

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Favourites ({self.user_profile})"
