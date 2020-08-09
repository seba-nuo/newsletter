from django.shortcuts import render

from newsletters.models import Newsletter
from rest_framework import status, viewsets
from newsletters.serializers import NewsletterSerializer

# Create your views here.



class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
