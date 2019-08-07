import os

from django.db import models
from random import random


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(filepath)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(0, 3000)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    print(new_filename, final_filename, ext)
    return f"products/{new_filename}/{final_filename}"

class Product(models.Model):    #Product_category
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places = 2, max_digits = 10, default=39.99)
    # image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # objects = ProductManager()
    #
    # def get_absolute_url(self):
    #     return reverse("products:detail", kwargs={"slug": self.slug})
    #
    # def __str__(self):
    #     return self.title
    #
    # @property
    # def name(self):
    #     return self.title
