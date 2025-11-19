from django.shortcuts import render

from .models import Product
from rest_framework import viewsets
from .serializer import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer  
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'category'] 
    