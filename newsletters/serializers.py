from newsletters.models import Newsletter, Vote, Tag
from rest_framework import serializers


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = [ 'id', 'name', 'description', 'image', 'target', 'frequency', 'created_at']
    

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'user', 'newsletter', 'created_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_at']


