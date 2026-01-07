from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
class HomePage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    banner_image = models.ImageField(
    upload_to="home/banner/",
    default="home/default_banner.jpg"  # this will be used for existing rows
)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Home Page Content"

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page"

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="doctors/", blank=True, null=True)
    highest_degree = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField(blank=True, null=True)
    details = models.TextField(blank=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
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

    # Service attributes
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="services/", blank=True, null=True)
    extra_info = RichTextField(blank=True)

    def clean(self):
        """
        Enforce max depth = 2
        - Parent can exist
        - Parent's parent MUST be None
        """
        if self.parent and self.parent.parent:
            raise ValidationError(
                "Services can only be nested up to 2 levels. "
                "You cannot assign a parent that already has a parent."
            )

    def save(self, *args, **kwargs):
        self.full_clean()  # 🔒 ensures clean() is always enforced

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} → {self.name}"
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)  # anyone: patient, doctor, staff
    designation = models.CharField(max_length=100, blank=True)  # free-text input
    message = models.TextField()
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)
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
    subject = models.CharField(max_length=200, default='')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.subject}"

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
