from django.db import models
from auths.models import User
from newsletters.models import Newsletter                 
from django.utils import timezone

# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='susbscriptions')
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='subscriptions')
    created = models.DateTimeField(auto_created=timezone.now)
    class Meta:
        unique_together = ('user', 'newsletter',)

    def __str__(self):
        return self.newsletter.name + " " + self.user.first_name 