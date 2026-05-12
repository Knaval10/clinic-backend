from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = RichTextField(blank=True)

    image = CloudinaryField("about_us_image", blank=True, null=True)

    journey_title = models.CharField(max_length=200, blank=True, default="Our Journey")
    journey_subtitle = models.CharField(
        max_length=300,
        blank=True,
        default="From humble beginnings to a leading healthcare institution",
    )
    journey_description = RichTextField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Us Content"

    class Meta:
        db_table = "core_aboutus"
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class Milestone(models.Model):
    about_us = models.ForeignKey(
        AboutUs, on_delete=models.CASCADE, related_name="milestones"
    )
    year = models.CharField(max_length=20)
    event = models.TextField()

    def __str__(self):
        return f"{self.year} - Milestone"

    class Meta:
        db_table = "core_milestone"


class Leader(models.Model):
    about_us = models.ForeignKey(
        AboutUs, on_delete=models.CASCADE, related_name="leaders"
    )
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = CloudinaryField("leader_image", blank=True, null=True)
    nmc_number = models.CharField(max_length=50, blank=True, null=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "core_leader"
