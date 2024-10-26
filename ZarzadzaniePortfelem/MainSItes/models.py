from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    pin = models.IntegerField(max_length=8)
    key = models.FloatField()

class UsersAccount(models.Model):
    balance = models.FloatField()
    history = models.CharField()
    borrowed = models.FloatField()
    UserKey = models.ForeignKey(User, on_delete=models.CASCADE)

class placeholder(models.Model):
    pass