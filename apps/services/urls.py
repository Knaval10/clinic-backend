from django.urls import path

from .views import ServiceListAPIView, ServicesDetailAPIView

urlpatterns = [
    path("services/", ServiceListAPIView.as_view(), name="api-services-list"),
    path("services/<slug:slug>/", ServicesDetailAPIView.as_view(), name="api-services-detail"),
]
