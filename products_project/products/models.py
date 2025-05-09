from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    rent = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    no_of_bedrooms = models.IntegerField(validators=[MinValueValidator(1)])
    is_deleted = models.BooleanField(default=False)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name