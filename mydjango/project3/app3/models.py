from django.db import models

# Create your models here.
class Hostel(models.Model):
    name=models.CharField(max_length=20)
    room=models.CharField(max_length=10)
    year=models.CharField(max_length=10)
