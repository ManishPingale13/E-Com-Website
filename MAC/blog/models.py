from django.db import models

# Create your models here.

class Blogpost(models.Model):
    postId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head0 = models.CharField(max_length=500,default="")
    head1 = models.CharField(max_length=500,default="")
    head2 = models.CharField(max_length=500,default="")
    cHead0 = models.CharField(max_length=500,default="")
    cHead1 = models.CharField(max_length=500,default="")
    cHead2 = models.CharField(max_length=500,default="")
    thumbnail = models.ImageField(upload_to="shop/images",default="")
    publishDate = models.DateField()

    def __str__(self):
        return self.title