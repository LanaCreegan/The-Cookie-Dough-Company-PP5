from django.db import models
from django.contrib.auth.models import User

from products.models import Product

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="review")
    name = models.CharField(null=True, blank=True, max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Product {self.review} by {self.name}"
