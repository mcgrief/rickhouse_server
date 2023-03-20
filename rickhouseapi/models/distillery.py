from django.db import models


class Distillery(models.Model):

    name = models.CharField(max_length=50)
    whiskey = models.ManyToManyField("Whiskey", through="WhiskeyDistillery")
    