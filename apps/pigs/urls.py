from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'pigs'

router = routers.DefaultRouter()
router.register('', views.PigViewSet, basename='porcos')

urlpatterns = [
    path('', include(router.urls) )
]