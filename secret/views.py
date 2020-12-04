from rest_framework import viewsets
from .serializers import SecretSerializer
from .models import Secret

class SecretViewSet(viewsets.ModelViewSet):
    queryset = Secret.objects.all()
    serializer_class = SecretSerializer