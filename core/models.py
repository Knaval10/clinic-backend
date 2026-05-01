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
        return self.title if self.title else f"Home Page Slide {self.id}"

    class Meta:
        verbose_name = "Home Page Slide"
        verbose_name_plural = "Home Page Slides"


class Doctor(models.Model):
    name = models.CharField(max_length=100)

    image = CloudinaryField(
        "doctor_image",
        blank=True,
        null=True
    )

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
        ordering = ['order']
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
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email} - {self.subject}"

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"


class AboutUs(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = RichTextField(blank=True)

    image = CloudinaryField(
        "about_us_image",
        blank=True,
        null=True
    )

    journey_title = models.CharField(max_length=200, blank=True, default="Our Journey")
    journey_subtitle = models.CharField(max_length=300, blank=True, default="From humble beginnings to a leading healthcare institution")
    journey_description = RichTextField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Us Content"

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class Milestone(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name="milestones")
    year = models.CharField(max_length=20)
    event = models.TextField()

    def __str__(self):
        return f"{self.year} - Milestone"


class Leader(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name="leaders")
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = CloudinaryField(
        "leader_image",
        blank=True,
        null=True
    )
    nmc_number = models.CharField(max_length=50, blank=True, null=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name

