from django.db import models
from django.utils import timezone

# Create your models here.

class Newsletter(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    target = models.IntegerField(null=False)
    frequency = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_created=timezone.now)

    def __str__(self):
        return self.name
