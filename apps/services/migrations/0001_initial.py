import ckeditor.fields
import cloudinary.models
import django.db.models.deletion
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
                    name="Service",
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
                        ("slug", models.SlugField(blank=True, max_length=120, unique=True)),
                        ("description", models.TextField(blank=True)),
                        (
                            "image",
                            cloudinary.models.CloudinaryField(
                                blank=True,
                                max_length=255,
                                null=True,
                                verbose_name="service_image",
                            ),
                        ),
                        ("extra_info", ckeditor.fields.RichTextField(blank=True)),
                        (
                            "parent",
                            models.ForeignKey(
                                blank=True,
                                null=True,
                                on_delete=django.db.models.deletion.CASCADE,
                                related_name="sub_services",
                                to="services.service",
                            ),
                        ),
                    ],
                    options={
                        "db_table": "core_service",
                        "verbose_name": "Service",
                        "verbose_name_plural": "Services",
                    },
                ),
            ],
        ),
    ]
