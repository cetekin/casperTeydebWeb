from django.db import models


class FileModel(models.Model):
    file = models.FileField()


def __str__(self):
    return self.file
