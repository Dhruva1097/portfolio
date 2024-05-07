from django.db import models

# Create your models here.
class Result(models.Model):
    name = models.CharField(max_length=100)
    eng = models.IntegerField()
    hin = models.IntegerField()
    maths = models.IntegerField()
    sci = models.IntegerField()
    cs = models.IntegerField()
    total = models.IntegerField()
    perc = models.IntegerField()
    res = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)