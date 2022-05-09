from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

class table():
    firstn = models.CharField(max_length=100)
    lastn = models.CharField(max_length=100)

class cards():
    img = models.ImageField(upload_to='pics')
    desc = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
