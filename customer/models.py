from django.db import models
from django.contrib.auth.models import User


""" To-Do:
- Customer
    - Name - Char | Done   
    - Email - unique | Done
"""


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

