from rest_framework import generics

from .models import Testimonial
from .serializers import TestimonialSerializer


class TestimonialListAPIView(generics.ListAPIView):
    queryset = Testimonial.objects.filter(is_approved=True).order_by("-created_at")
    serializer_class = TestimonialSerializer
    authentication_classes = []
    permission_classes = []
