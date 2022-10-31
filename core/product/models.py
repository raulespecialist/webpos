from django.conf import settings
from django.db import models
from django.utils import timezone


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    code_number = models.IntegerField(verbose_name='Bar Code')
    image = models.ImageField(upload_to='products/')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title