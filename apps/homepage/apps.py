from django.apps import AppConfig


class HomepageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.homepage"
    label = "homepage"
    verbose_name = "Home Page"
