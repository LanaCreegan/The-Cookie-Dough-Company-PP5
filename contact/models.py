from django.db import models

class Contact(models.Model):
    """
    Model to let users send a message 
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
