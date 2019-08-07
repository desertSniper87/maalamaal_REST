from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .models import Product #, ProductType
from .serializers import ProductSerializer #, ProductTypeSerializer


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductTypeViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows products to be viewed or edited.
#     """
#     queryset = ProductType.objects.all()
#     serializer_class = ProductTypeSerializer
