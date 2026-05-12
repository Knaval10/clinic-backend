from rest_framework import generics

from .models import Doctor
from .serializers import DoctorDetailSerializer, DoctorOverviewSerializer


class DoctorListAPIView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorOverviewSerializer
    authentication_classes = []
    permission_classes = []


class DoctorDetailAPIView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer
    lookup_field = "slug"
    authentication_classes = []
    permission_classes = []
