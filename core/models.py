from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

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

class ServicesMenus(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="sub_menus"
    )
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} → {self.name}"
        return self.name

    class Meta:
        verbose_name = "Service Menu"
        verbose_name_plural = "Service Menus"

class Services(models.Model):
    menu = models.OneToOneField(
        ServicesMenus,
        on_delete=models.CASCADE,
        related_name="service"
    )
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="services/", blank=True, null=True)
    extra_info = RichTextField(blank=True)  # <-- WYSIWYG editor

    def __str__(self):
        return f"Service content for {self.menu.name}"

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
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
