from django.urls import path, include
from rest_framework import routers
from secret.views import SecretViewSet

router = routers.DefaultRouter()
router.register(r'secrets', SecretViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
