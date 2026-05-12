from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.db import models

from apps.common.utils import generate_unique_slug


class Doctor(models.Model):
    name = models.CharField(max_length=100)

    image = CloudinaryField("doctor_image", blank=True, null=True)

    highest_degree = models.CharField(max_length=100)
    nmc_number = models.CharField(max_length=50, blank=True, null=True)
    years_of_experience = models.PositiveIntegerField(blank=True, null=True)

    order = models.PositiveIntegerField(default=0)

    details = RichTextField(blank=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, "name")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "core_doctor"
        ordering = ["order"]
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
