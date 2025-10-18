from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'horses'

router = routers.DefaultRouter()
router.register('', views.CategoryViewSet, basename='cavalos')

urlpatterns = [
    path('', include(router.urls) )
    path('cavalos/', include('horses.urls', namespace='horses')),
]
