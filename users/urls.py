from django.conf.urls import url
from .views import CreateUserAPIView, authenticate_user, UserRetrieveUpdateAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r'^obtain_token/', authenticate_user)

urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^obtain_token/$', authenticate_user),
    # =url(r'^/', include(router.urls)),
    # url(r'^obtain_token/$', authenticate_user)
    # url(r'^obtain_token/$', 'authenticate_user', name='authenticate_user')
]