from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to = 'appcoolshop')

class Product(models.Model):
    img = models.ImageField(upload_to = 'appcoolshop')
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



