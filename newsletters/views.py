from django.shortcuts import render

from newsletters.models import Newsletter, Vote, Tag
from rest_framework import status, viewsets
from newsletters.serializers import NewsletterSerializer, VoteSerializer, TagSerializer


# Create your views here.


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


