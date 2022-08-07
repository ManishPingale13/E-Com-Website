from django.db import models

class Product(models.Model):
    productId = models.AutoField
    productName = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subCategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images",default="")
    desc = models.CharField(max_length=300)
    publishDate = models.DateField()

    def __str__(self):
        return self.productName