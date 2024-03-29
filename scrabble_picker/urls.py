from django.urls import include, path
from rest_framework import routers
from scrabble_picker.core import views

router = routers.DefaultRouter()
router.register(r'games', views.GameViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
