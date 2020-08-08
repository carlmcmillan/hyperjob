from django.db import models
from django.db.models import CharField, ForeignKey
from django.contrib.auth.models import User


class Resume(models.Model):
    description = CharField(max_length=1024)
    author = ForeignKey(User, on_delete=models.CASCADE)
