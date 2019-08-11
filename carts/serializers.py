from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Cart


class CartSerializer(serializers.HyperlinkedModelSerializer):
    total = serializers.ReadOnlyField()
    class Meta:
        model = Cart
        fields = ['product', 'quantity', 'total']

    def __init__(self, *args, **kwargs):
        super(CartSerializer, self).__init__(*args, **kwargs)



