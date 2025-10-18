from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'dogs'

router = routers.DefaultRouter()
router.register('', views.DogViewSet, basename='cachorros')

urlpatterns = [
    path('', include(router.urls) )
]