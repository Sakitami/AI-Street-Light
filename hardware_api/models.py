from uuid import uuid4
from django.db import models


class Light(models.Model):
    light_id = models.UUIDField(default=uuid4, editable=False, unique=True)
    air_index = models.FloatField()
    pm25_index = models.FloatField()
    status = models.BooleanField(default=False)
    group = models.IntegerField()
    rgb = models.CharField(max_length=9, default='858585')
    edit_flag = models.BooleanField(default=False)
