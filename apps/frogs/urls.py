from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'frogs'

router = routers.DefaultRouter()
router.register('', views.FrogViewSet, basename='frogs')

urlpatterns = [
    path('', include(router.urls) )
]