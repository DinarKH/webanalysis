from django.db import models

# Create your models here.

class dataset(models.Model):
    link = models.CharField(max_length=200)
    sentiment = models.IntegerField()