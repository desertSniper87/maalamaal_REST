from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    order_total = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')
    cart = serializers.HyperlinkedIdentityField(
        read_only=True,
        many=True, view_name='cart-detail'
    )
    paid = serializers.ReadOnlyField()


    class Meta:
        model = Order
        fields = ['order_total', 'user', 'paid', 'cart']


