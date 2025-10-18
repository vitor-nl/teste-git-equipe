from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'lions'

router = routers.DefaultRouter()
router.register('', views.LionViewSet, basename='lions')

urlpatterns = [
    path('', include(router.urls) )
]