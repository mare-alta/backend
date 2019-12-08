from django.db import models
from django.conf import settings


class Level(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=100)


class Complaint(models.Model):
    id = models.AutoField(primary_key=True)
    user_hash = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    level = models.ForeignKey(Level, null=True, on_delete=models.CASCADE)
