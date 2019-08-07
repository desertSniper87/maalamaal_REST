from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'date_created', 'Product_type', 'Product_attributes')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super(ProductSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        return super(ProductSerializer, self).update(instance, validated_data)

