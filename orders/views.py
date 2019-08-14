from rest_framework import viewsets, status
from rest_framework.response import Response

from orders.models import Order
from orders.serializers import OrderSerializer
from carts.models import Cart


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        user_carts = Cart.objects.filter(user=user)
        order_total = 0

        for cart in user_carts:
            cart.ordered = True
            order_total += cart.total
            cart.save()

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




