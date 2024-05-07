from django.db import models

# Create your models here.
class users(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # res = models.CharField(max_length=100)
    # grade = models.CharField(max_length=100)