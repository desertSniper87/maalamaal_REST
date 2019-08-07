from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
  user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
  role = models.CharField(choices=['buyer', 'seller'])