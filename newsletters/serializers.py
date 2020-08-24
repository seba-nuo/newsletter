from newsletters.models import Newsletter, Vote, Tag, NewsletterTag
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
        fields = ['id', 'name', 'slug', 'created_at']

class NewsletterTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterTag
        fields = ['id', 'newsletter', 'tag' ]


