from django.contrib.auth.models import User
from django.db import models

from orders.models import Order
from products.models import Product


class Cart(models.Model):
    """Docstring for Cart. """
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) # buyer
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(blank=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    ordered = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.product is not None:
            self.total = self.product.price_taka * self.quantity
        return super(Cart, self).save(*args, **kwargs)

    @property
    def seller(self):
        return self.product.seller



