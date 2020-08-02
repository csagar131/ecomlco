from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Product

class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
