
# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from auths.models import User
from rest_framework import status, viewsets
from auths.serializers import UserCreateSerializer
from rest_framework.decorators import action
from subscriptions.serializers import SubscriptionSerializer
from subscriptions.models import Subscription
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    return Response(data="Only for Looged in User", status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


    @action(detail=True, methods=['GET'])
    def subscriptions(self, request, pk=None):
        if request.method == 'GET':
            user = self.get_object()
            subscriptions = Subscription.objects.filter(user=user)
            serialized = SubscriptionSerializer(subscriptions, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)

