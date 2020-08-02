from django.shortcuts import render
from .serializers import CategorySerializer
from .models import Category
from rest_framework import viewsets


class CategoryModelViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()




