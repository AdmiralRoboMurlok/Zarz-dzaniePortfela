from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    pin = models.IntegerField()
    key = models.FloatField()

class UsersAccount(models.Model):
    balance = models.FloatField()
    history = models.CharField(max_length=1260) #spytać się jak robić listy w modelach django
    borrowed = models.FloatField()
    UserKey = models.ForeignKey(User, on_delete=models.CASCADE)

class Bank(models.Model):
    balance = models.FloatField()
    loans = models.FloatField()

class placeholder(models.Model):
    pass