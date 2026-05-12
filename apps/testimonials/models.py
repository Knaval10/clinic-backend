from cloudinary.models import CloudinaryField
from django.db import models


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True)
    message = models.TextField()

    image = CloudinaryField("testimonial_image", blank=True, null=True)

    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.designation})" if self.designation else self.name

    class Meta:
        db_table = "core_testimonial"
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
