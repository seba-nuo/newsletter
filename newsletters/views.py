from django.shortcuts import render

from newsletters.models import Newsletter, Vote, Tag, NewsletterTag
from rest_framework import status, viewsets
from newsletters.serializers import NewsletterSerializer, VoteSerializer, TagSerializer, NewsletterTagSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    parser_class = (MultiPartParser,)

    


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(detail=True, methods=['GET'])
    def newsletters(self, request, pk=None):
        if request.method == 'GET':
            tag = self.get_object()
            newsletters_tagged = NewsletterTag.objects.filter(tag=tag)
            serialized = NewsletterTagSerializer(newsletters_tagged, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)


class NewsletterTagViewSet(viewsets.ModelViewSet):
    queryset = NewsletterTag.objects.all()
    serializer_class = NewsletterTagSerializer

