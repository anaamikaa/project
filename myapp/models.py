from django.db import models


# Create your models here.
class signup(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)

