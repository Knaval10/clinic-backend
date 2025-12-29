from django.urls import path
from .views import HomePageAPIView, TestimonialListAPIView, DoctorListAPIView, DoctorDetailAPIView, ServicesMenusListAPIView, ServicesDetailAPIView

urlpatterns = [
    path("home/", HomePageAPIView.as_view(), name="api-home"),
    path("testimonials/", TestimonialListAPIView.as_view(), name="api-testimonials"),
    path("doctors/", DoctorListAPIView.as_view(), name="api-doctors"),
    path("doctors/<slug:slug>/", DoctorDetailAPIView.as_view(), name="api-doctor-detail"),
     path("services-menus/", ServicesMenusListAPIView.as_view(), name="api-services-menus"),
    path("services/<slug:menu__slug>/", ServicesDetailAPIView.as_view(), name="api-services-detail"),

]

