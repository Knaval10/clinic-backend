"""Project URL configuration.

Each feature app under ``apps/`` exposes its own ``urls.py``. We include
them twice, once under ``/`` and once under ``/api/``, to preserve the
existing public URLs.
"""
from django.contrib import admin
from django.urls import include, path


feature_urls = [
    path("", include("apps.homepage.urls")),
    path("", include("apps.doctors.urls")),
    path("", include("apps.services.urls")),
    path("", include("apps.testimonials.urls")),
    path("", include("apps.contact.urls")),
    path("", include("apps.aboutus.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(feature_urls)),
    path("", include(feature_urls)),
]
