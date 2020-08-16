from django.shortcuts import render
from django.core.mail import EmailMessage
from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionSerializer
from rest_framework import viewsets
from auths.models import User
from django.core.mail import send_mail
# Create your views here.

def send_email():
    email = EmailMessage(
        'Title',
        'Hola',
        'pruebaspruebas2020aca@gmail.com',
        ['smartechbeat@gmail.com'],
    )
    email.send()


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


    def create(self, request, *args, **kwargs):
        response = super(SubscriptionViewSet, self).create(request, *args, **kwargs)
        send_email()  # sending mail
        return response
