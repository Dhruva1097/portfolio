from django.db import models

# Create your models here.
class contacts(models.Model):
    f_name = models.CharField(max_length=100, default='')
    l_name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=100, default='')
    nickname = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    address = models.CharField(max_length=500, default='')
    client_id = models.CharField(max_length=100, default='')