from django.db import models


""" To-Do:
- Customer
    - Name - Char | Done   
    - Email - unique | Done
"""


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)

