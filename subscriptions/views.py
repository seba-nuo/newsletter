from django.shortcuts import render
from django.core.mail import EmailMessage
from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionSerializer, SubscriptionDetailSerializer
from rest_framework import viewsets
from auths.models import User
from newsletters.models import Newsletter,Vote
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response


# Create your views here.

def send_email(myemail):
    email = EmailMessage(
        'Title',
        'Hola',
        '********@gmail.com',
        [myemail],
    )
    email.send()


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


    def get_serializer_class(self):
        if self.action == 'list':
            return SubscriptionDetailSerializer
        return SubscriptionSerializer

    def create(self, request, *args, **kwargs):
        newsletter = Newsletter.objects.filter(id=request.data['newsletter'])
        target_found = newsletter.values()
        my_target = target_found[0]['target']
        votes_filtered = Vote.objects.filter(newsletter=request.data['newsletter'])
        
        if (len(votes_filtered)) < my_target:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED) 

        user_id = request.data['user']
        user = User.objects.filter(id=user_id)
        my_user = user.values()
        user_email = my_user[0]['email']
        response = super(SubscriptionViewSet, self).create(request, *args, **kwargs)
        send_email(user_email)
        return response