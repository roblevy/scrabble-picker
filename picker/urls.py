from django.urls import include
from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'games', views.GameViewSet)

urlpatterns = [
    path('games', include(router.urls))
]
