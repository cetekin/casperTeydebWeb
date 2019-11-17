from django.db import models
from djongo.models import fields

class OpinionMiningResults(models.Model):
    _id = fields.ObjectIdField()
    aspectStats = models.TextField()
    deviceName = models.TextField(default="noName")
    reportDate = models.TextField(default="noDate")
    textCount = models.IntegerField()
