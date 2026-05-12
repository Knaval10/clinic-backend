from cloudinary.models import CloudinaryField
from django.db import models


class HomePage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)

    banner_image = CloudinaryField("banner_image", blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title if self.title else f"Home Page Slide {self.id}"

    class Meta:
        db_table = "core_homepage"
        verbose_name = "Home Page Slide"
        verbose_name_plural = "Home Page Slides"
