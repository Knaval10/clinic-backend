from django.urls import path
from .views import (
    HomePageAPIView,
    TestimonialListAPIView,
    DoctorListAPIView,
    DoctorDetailAPIView,
    ServiceListAPIView,      
    ServicesDetailAPIView,
    contact_message_create     
)

urlpatterns = [
    path("home/", HomePageAPIView.as_view(), name="api-home"),
    path("testimonials/", TestimonialListAPIView.as_view(), name="api-testimonials"),
    path("doctors/", DoctorListAPIView.as_view(), name="api-doctors"),
    path("doctors/<slug:slug>/", DoctorDetailAPIView.as_view(), name="api-doctor-detail"),

    # Top-level services list (with sub-services)
    path("services/", ServiceListAPIView.as_view(), name="api-services-list"),

    # Single service detail by slug
    path("services/<slug:slug>/", ServicesDetailAPIView.as_view(), name="api-services-detail"),
    path('api/contact/', contact_message_create, name='contact-message-create'),
]
