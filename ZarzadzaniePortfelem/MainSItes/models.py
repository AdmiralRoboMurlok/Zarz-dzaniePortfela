from django.db import models

# Create your models here.
class FRBS(models.Model):
    pin = models.IntegerField()

class UsersAccount(models.Model):
    balance = models.FloatField()
    borrowed = models.FloatField()

class Bank(models.Model):
    balance = models.FloatField()
    loans = models.FloatField()
    UserKey = models.ForeignKey(FRBS, on_delete=models.CASCADE)

class Histroy(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateTimeField()