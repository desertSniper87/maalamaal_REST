from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from products.models import ProductCategory
from products.serializers import ProductCategorySerializers
from .models import Product #, ProductType
from .serializers import ProductSerializer #, ProductTypeSerializer


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product categories to be viewed or edited.
    """
    http_method_names = ['get', 'head']
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializers
