from django.db import models

# Create your models here.
class User(models.Model):
    pin = models.IntegerField()

class UsersAccount(models.Model):
    balance = models.FloatField()
    borrowed = models.FloatField()
    UserKey = models.ForeignKey(User, on_delete=models.CASCADE)

class Bank(models.Model):
    balance = models.FloatField()
    loans = models.FloatField()

class Histroy(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateTimeField()
    UserKey = models.ForeignKey(User, on_delete=models.CASCADE)

class placeholder(models.Model):
    pass