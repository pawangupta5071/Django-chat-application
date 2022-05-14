from django.db import models
from pytz import timezone
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f'), blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)