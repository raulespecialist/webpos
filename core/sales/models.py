from django.conf import settings
from django.db import models
from django.utils import timezone
from product.models import Product

# Create your models here.

PAYMENT_CHOICES = (
    ("Cash payment", "1"),
    ("Credit Card", "2"),
    ("Transfer", "3"),
)

STATUS_CHOICES = (
    ("Processing", "1"),
    ("Completed", "2"),
    ("Aborted", "3"),
)


class Invoice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    pay_type = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default='1'
    )
    created_date = models.DateTimeField(
        default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='1'
    )
    note = models.TextField()

    def __str__(self):
        return str(self.pk)


class Item(models.Model):
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    code_number = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='code_numer')
    name = models.CharField(default='', max_length=240)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    sum_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name
