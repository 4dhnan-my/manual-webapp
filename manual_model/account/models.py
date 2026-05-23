from django.db import models

class User(models.Model):
    username = models.CharField(max_length=180)
    email = models.EmailField()
    password = models.CharField(max_length=180)


def __str__(self):
    return self.username
