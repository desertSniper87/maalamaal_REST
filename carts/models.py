from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save

from orders.models import Order
from products.models import Product


class Cart(models.Model):
    """Docstring for Cart. """
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
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

# def pre_save_cart_receiver(sender, instance, action, *args, **kwargs):
#     # if not instance.slug:
#         # instance.slug = unique_slug_generator(instance)
#     print("action: ", action)
#     print("instance.products: ", instance.products.all())
#     print("instance.total: ", instance.total)
#     if action=='post_add' or action=='post_remove' or action=='post_clear':
#         products = instance.products.all()
#         total = 0
#
#         for x in products:
#             print("x: ", x)
#             total += x.price
#
#         print('total: ', total)
#         instance.total = total
#         instance.save()

# pre_save.connect(pre_save_cart_receiver, sender=Cart)

# m2m_changed.connect(m2m_save_cart_receiver, sender=Cart.products.through)



