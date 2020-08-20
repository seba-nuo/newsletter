from django.shortcuts import render

from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionSerializer
from rest_framework import viewsets

# Create your views here.


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

