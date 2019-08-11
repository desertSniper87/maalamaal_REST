from rest_framework import viewsets

from orders.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Order.objects.all()
    # serializer_class = OrderSerializer