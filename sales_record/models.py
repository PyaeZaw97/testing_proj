from django.db import models

# Create your models here.
class Info(models.Model):
    customer_name=models.CharField(max_length=255)
    customer_ph=models.CharField(max_length=11)
    items=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    branch=models.CharField(max_length=255)
    paid=models.BooleanField(default=False)
    date=models.DateField()

    def __str__(self):
        return self.customer_name
