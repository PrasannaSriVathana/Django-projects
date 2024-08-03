from django.db import models

# Create your models here.
class Bank(models.Model):
    accno = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=10)
    balance = models.CharField(max_length=40)


