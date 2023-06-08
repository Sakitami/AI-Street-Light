from django.db import models


# Create your models here.

class Group(models.Model):
    group_id = models.IntegerField(editable=False, unique=True)
    group_name = models.CharField(max_length=20)
    group_location = models.CharField(max_length=20)
    group_longitude = models.FloatField()
    group_latitude = models.FloatField()
    group_status = models.BooleanField(default=False)


class User(models.Model):
    user_id = models.IntegerField(editable=False, unique=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    salt = models.CharField(max_length=8)


class UserGroup(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()
