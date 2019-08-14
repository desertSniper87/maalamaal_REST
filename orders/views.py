from django.db import transaction
from django.dispatch import Signal
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer
from carts.models import Cart


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        user = request.user
        user_carts = Cart.objects.filter(user=user, ordered=False)
        order_total = 0

        for cart in user_carts:
            cart.ordered = True
            order_total += cart.total
            cart.save(delete_old_cart=False)

            cart.product.available_quantity -= cart.quantity
            cart.product.save()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        serializer.save(
            user=user,
            order_total=order_total,
            carts=user_carts,
            paid=True
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def list(self, request, *args, **kwargs):
    #     return super(OrderViewSet, self).list(request, *args, **kwargs)





