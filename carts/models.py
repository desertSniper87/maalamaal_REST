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
            max_quantity = self.product.available_quantity
            try:
                prev_cart = Cart.objects.get(user=self.user, product=self.product)
                if prev_cart.quantity + self.quantity <= max_quantity:
                    prev_cart.quantity += self.quantity
                    prev_cart.total += float(prev_cart.product.price_taka * prev_cart.quantity)
                    return prev_cart
            except Cart.DoesNotExist:
                pass
            self.total += float(self.product.price_taka * self.quantity)
        return super(Cart, self).save(*args, **kwargs)

    @property
    def seller(self):
        return self.product.seller



