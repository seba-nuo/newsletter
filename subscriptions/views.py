from django.shortcuts import render
from django.core.mail import EmailMessage
from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionSerializer, SubscriptionDetailSerializer
from rest_framework import viewsets
from auths.models import User
from newsletters.models import Newsletter
from django.core.mail import send_mail
# Create your views here.

def send_email():
    email = EmailMessage(
        'Title',
        'Hola',
        '**********@gmail.com',
        ['**********@gmail.com'],
    )
    email.send()


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


    # def get_queryset(self):
        
    #     subscriptions_filtered = Subject.objects.filter(**parameters)
    #     return subjects_filtered

    def get_serializer_class(self):
        if self.action == 'list':
            return SubscriptionDetailSerializer
        return SubscriptionSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        print(request.data['user'])
        newsletter = Newsletter.objects.filter(id=request.data['newsletter'])
        target_found = newsletter.values()
        my_target = target_found[0]['target']
        print(target_found)
        print(my_target)
        print(newsletter)
        user_id = request.data['user']
        user = User.objects.filter(id=user_id)
        print(user)
        response = super(SubscriptionViewSet, self).create(request, *args, **kwargs)
        send_email()  # sending mail
        return response
#EN EL QUERYSET DE UNA FILTRAR SOLO LOS QUE LLEGUEN AL TARGET. 
#TRAER EL SIZE DE LA LISTA. DE TODOS LOS VOTOS. FILTRADOS POR NEWSLETTER. 