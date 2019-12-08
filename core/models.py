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
    level_ml_model = models.CharField(max_length=100, default='BAIXO')
    insert_date = models.DateTimeField(auto_now=True)


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    complaint = models.ForeignKey(Complaint, null=True, on_delete=models.CASCADE)
    desc = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    insert_date = models.DateTimeField(auto_now=True)
