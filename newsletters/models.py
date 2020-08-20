from django.db import models
from django.utils import timezone

from auths.models import User

# Create your models here.

class Newsletter(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    target = models.IntegerField(null=False)
    frequency = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_created=timezone.now)

    def __str__(self):
        return self.name


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='votes')
    created_at = models.DateTimeField(auto_created=timezone.now)
    class Meta:
        unique_together = ('user', 'newsletter',)

    def __str__(self):
        return self.newsletter.name + " " + self.user.first_name 


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_created=timezone.now)
    
    def __str__(self):
        return self.name


class NewsLetter_Tag(models.Model):
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='related_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='newsletters_tagged')
    class Meta:
        unique_together = ('newsletter', 'tag',)

    def __str__(self):
        return self.newsletter.name + " " + self.tag.name