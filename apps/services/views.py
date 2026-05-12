from rest_framework import generics

from .models import Service
from .serializers import ServiceSerializer


class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.filter(parent__isnull=True)
    serializer_class = ServiceSerializer
    authentication_classes = []
    permission_classes = []


class ServicesDetailAPIView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "slug"
    authentication_classes = []
    permission_classes = []
