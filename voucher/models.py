from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
from customer.models import Customer
from django.utils.crypto import get_random_string



""" To-Do:
- Special Offer
    - Name - Char
    - percentage discount - Float with range

- Voucher Code
    - Unique randomly generated Code (at least 8 chars)
    - Assigned to a Customer and a special offer - Foreign Keys
    - Expiration Date - Date
        - property: is_expired - calculated
    - Can just be used once - Boolean is_used
    - Should track date of usage - used_date
    - If code ABC generated for a@example.com then it can never be generated for anyone else - Unique Code
    - One email can have one or more vouchers - One2Many
    - If the expiration date is 6-May then the code is valid till 6-May at 23:59
    - the minimum and maximum possible discounts between 5% and 100%

"""

PERCENTAGE_VALIDATOR = [MinValueValidator(1), MaxValueValidator(100)]


def generate_random_string(length):
    code = get_random_string(length=length)
    return code.upper()


class Offer(models.Model):
    name = models.CharField(max_length=255)
    discount_percentage = models.DecimalField(max_digits=3, decimal_places=0, default=0.0,
                                              validators=PERCENTAGE_VALIDATOR)

    def __str__(self):
        return self.name


class Voucher(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=16, unique=True, blank=True, default=generate_random_string(length=8))
    is_used = models.BooleanField(default=False)
    expire_date = models.DateField()
    used_date = models.DateField(null=True, blank=True)


    @property
    def is_expired(self):
        diff_days = (self.expire_date - date.today()).days
        return True if diff_days < 0 else False

    def __str__(self):
        return f'Code: {self.code} - {"Expired" if self.is_expired else "Active"} - {self.offer.name} - {self.customer.email}'






