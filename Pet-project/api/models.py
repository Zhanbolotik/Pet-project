from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2,)
    description = models.TextField()
    stars = models.IntegerField()

    def __str__(self):
        return self.name