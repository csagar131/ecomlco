from django.db import models
from api.user.models import User
from api.product.models import Product
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null = True, blank = True)

    product_names = models.CharField(max_length = 500)
    totol_products = models.CharField(max_length = 500, default = 0)
    transaction_id = models.CharField(max_length = 150, default = 0)
    total_amount = models.CharField(max_length = 40, default = 0)

    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)