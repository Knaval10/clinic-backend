from django.urls import path

from .views import TestimonialListAPIView

urlpatterns = [
    path("testimonials/", TestimonialListAPIView.as_view(), name="api-testimonials"),
]
