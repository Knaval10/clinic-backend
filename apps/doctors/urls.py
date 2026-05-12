from django.urls import path

from .views import DoctorDetailAPIView, DoctorListAPIView

urlpatterns = [
    path("doctors/", DoctorListAPIView.as_view(), name="api-doctors"),
    path("doctors/<slug:slug>/", DoctorDetailAPIView.as_view(), name="api-doctor-detail"),
]
