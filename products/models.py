import os
from django.contrib.auth.models import User

from django.db import models
from random import randint


# def get_filename_ext(filepath):
#     base_name = os.path.basename(filepath)
#     name, ext = os.path.splitext(filepath)
#     return name, ext

# def upload_image_path(instance, filename):
#     new_filename = randint(0, 3000)
#     name, ext = get_filename_ext(filename)
#     final_filename = f'{new_filename}{ext}'
#     print(new_filename, final_filename, ext)
#     return f"products/{new_filename}/{final_filename}"

class ProductCategory(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=120)
    description = models.TextField()
    # slug = models.SlugField(blank=True, unique=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    available_quantity = models.IntegerField(default=0)
    price_taka = models.DecimalField(decimal_places = 2, max_digits = 10, default=39.99)
    category = models.ForeignKey(ProductCategory,
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True)

    # objects = ProductManager()
    #
    # def get_absolute_url(self):
    #     return reverse("products:detail", kwargs={"slug": self.slug})
    #
    def __str__(self):
        return self.name
    #
    # @property
    # def name(self):
    #     return self.title
