from django.db import models

class Product(models.Model):
    productId = models.AutoField
    productName = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    publishDate = models.DateField()