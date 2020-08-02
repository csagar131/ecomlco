from django.db import models
from api.category.models import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 255)
    price = models.IntegerField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default = True)
    image = models.ImageField(upload_to = 'images/', blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, null = True)

    def __str__(self):
        return self.name