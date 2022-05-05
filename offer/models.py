from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


""" To-Do:
- Special Offer
    - Name - Char
    - percentage discount - Float with range
        - Can be 0?
        
"""

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    discount_percentage = models.DecimalField(max_digits=3, decimal_places=0, default=0.0, validators=PERCENTAGE_VALIDATOR)

