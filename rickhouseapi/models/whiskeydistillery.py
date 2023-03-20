from django.db import models
from .distillery import Distillery
from .whiskey import Whiskey


class WhiskeyDistillery(models.Model):

    distillery = models.ForeignKey(Distillery, on_delete=models.CASCADE)
    whiskey = models.ForeignKey(Whiskey, on_delete=models.CASCADE, related_name = "joined_whiskey")
    class Meta: 
        unique_together = ('whiskey', 'distillery')
    