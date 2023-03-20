from django.db import models
from .user import User
from .whiskey_type import Type


class Whiskey(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    year = models.IntegerField()
    proof =models.IntegerField()
    label = models.CharField(max_length=50)
    