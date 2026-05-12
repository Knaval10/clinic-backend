import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core", "0022_split_models_out"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.CreateModel(
                    name="Testimonial",
                    fields=[
                        (
                            "id",
                            models.BigAutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        ("name", models.CharField(max_length=100)),
                        ("designation", models.CharField(blank=True, max_length=100)),
                        ("message", models.TextField()),
                        (
                            "image",
                            cloudinary.models.CloudinaryField(
                                blank=True,
                                max_length=255,
                                null=True,
                                verbose_name="testimonial_image",
                            ),
                        ),
                        ("is_approved", models.BooleanField(default=False)),
                        ("created_at", models.DateTimeField(auto_now_add=True)),
                    ],
                    options={
                        "db_table": "core_testimonial",
                        "verbose_name": "Testimonial",
                        "verbose_name_plural": "Testimonials",
                    },
                ),
            ],
        ),
    ]
