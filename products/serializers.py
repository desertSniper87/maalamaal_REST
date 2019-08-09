from django.contrib.auth.models import User, Group
from rest_framework import serializers

from products.models import ProductCategory
from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField()

    class Meta:
        model = Product
        fields = ('image', 'name', 'description', 'available_quantity', 'price_taka', 'category', 'timestamp')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['seller'] = user

        category = ProductCategory.objects.get(name=validated_data['category'])
        validated_data['category'] = category

        return super(ProductSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        return super(ProductSerializer, self).update(instance, validated_data)

class ProductCategorySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

