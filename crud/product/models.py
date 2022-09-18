from datetime import datetime
from django.db import models

# Create your models here.

class ProductApi(models.Model):
    title= models.CharField(max_length = 100)
    description= models.TextField()
    price= models.FloatField()

    def __str__(self):
         return self.title

class ProductDetails(models.Model):
    product = models.ForeignKey(ProductApi, on_delete=models.CASCADE, default=None, related_name="retervails_date")
    retervails_date = models.DateTimeField(default=datetime.now)
    retervails = models.IntegerField(default=0)

