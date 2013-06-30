from django.db import models

# Create your models here.
class Experiment(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=200)

