from django.db import models

# Create your models here.
class FRBS(models.Model):
    pin = models.IntegerField(default=0)

class UsersAccount(models.Model):
    balance = models.FloatField(default=0)
    borrowed = models.FloatField(default=0)

class Bank(models.Model):
    balance = models.FloatField(default=0)
    loans = models.FloatField(default=0)
    UserKey = models.ForeignKey(FRBS, on_delete=models.CASCADE)

class Histroy(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateTimeField()