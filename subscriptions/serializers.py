from rest_framework import serializers
from subscriptions.models import Subscription
from newsletters.serializers import NewsletterSerializer



class SubscriptionSerializer(serializers.ModelSerializer):
    # newsletter = NewsletterSerializer(read_only=False)

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'newsletter', 'created']


class SubscriptionDetailSerializer(serializers.ModelSerializer):
    newsletter = NewsletterSerializer(read_only=False)

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'newsletter', 'created']




