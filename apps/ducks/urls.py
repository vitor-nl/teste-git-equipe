from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ducks'

router = routers.DefaultRouter()
router.register('', views.DucksViewSet, basename='ducks')

urlpatterns = [
    path('', include(router.urls) )
]