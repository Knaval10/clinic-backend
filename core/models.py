from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField
import itertools


# ------------------ Helper ------------------
def generate_unique_slug(instance, field_name):
    base_slug = slugify(getattr(instance, field_name))
    slug = base_slug
    for i in itertools.count(1):
        if not type(instance).objects.filter(slug=slug).exists():
            return slug
        slug = f"{base_slug}-{i}"


# ------------------ Models ------------------

class HomePage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)

    banner_image = CloudinaryField(
        "banner_image",
        blank=True,
        null=True
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Home Page Content"

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page"


class Doctor(models.Model):
    name = models.CharField(max_length=100)

    image = CloudinaryField(
        "doctor_image",
        blank=True,
        null=True
    )

    highest_degree = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField(blank=True, null=True)
    details = models.TextField(blank=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, "name")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"


class Service(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="sub_services"
    )
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)

    image = CloudinaryField(
        "service_image",
        blank=True,
        null=True
    )

    extra_info = RichTextField(blank=True)

    def clean(self):
        if self.parent and self.parent.parent:
            raise ValidationError(
                "Services can only be nested up to 2 levels."
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.slug:
            self.slug = generate_unique_slug(self, "name")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.parent.name} → {self.name}" if self.parent else self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True)
    message = models.TextField()

    image = CloudinaryField(
        "testimonial_image",
        blank=True,
        null=True
    )

    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.designation})" if self.designation else self.name

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, default="", blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.subject}"

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
