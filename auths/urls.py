from django.urls import path, include
from auths import views
from django.conf.urls import url


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('restricted/', views.restricted) #url de prueba 

]
