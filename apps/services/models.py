from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.db import models

from apps.common.utils import generate_unique_slug


class Service(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="sub_services",
    )
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)

    image = CloudinaryField("service_image", blank=True, null=True)

    extra_info = RichTextField(blank=True)

    def clean(self):
        if self.parent and self.parent.parent:
            raise ValidationError("Services can only be nested up to 2 levels.")

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.slug:
            self.slug = generate_unique_slug(self, "name")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.parent.name} → {self.name}" if self.parent else self.name

    class Meta:
        db_table = "core_service"
        verbose_name = "Service"
        verbose_name_plural = "Services"
