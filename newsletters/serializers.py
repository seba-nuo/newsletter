from newsletters.models import Newsletter
from rest_framework import serializers


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = [ 'id', 'name', 'description', 'target', 'frequency', 'created_at']
