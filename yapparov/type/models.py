from django.db import models

class Stat(models.Model):
    title = models.CharField(max_length=50)
    subtile = models.CharField(max_length=200)
    URL = models.URLField(max_length=150)

