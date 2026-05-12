import ckeditor.fields
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
                    name="Doctor",
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
                        (
                            "image",
                            cloudinary.models.CloudinaryField(
                                blank=True,
                                max_length=255,
                                null=True,
                                verbose_name="doctor_image",
                            ),
                        ),
                        ("highest_degree", models.CharField(max_length=100)),
                        ("nmc_number", models.CharField(blank=True, max_length=50, null=True)),
                        ("years_of_experience", models.PositiveIntegerField(blank=True, null=True)),
                        ("order", models.PositiveIntegerField(default=0)),
                        ("details", ckeditor.fields.RichTextField(blank=True)),
                        ("slug", models.SlugField(blank=True, max_length=120, unique=True)),
                    ],
                    options={
                        "db_table": "core_doctor",
                        "ordering": ["order"],
                        "verbose_name": "Doctor",
                        "verbose_name_plural": "Doctors",
                    },
                ),
            ],
        ),
    ]
