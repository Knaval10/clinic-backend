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
                    name="AboutUs",
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
                        ("title", models.CharField(blank=True, max_length=200)),
                        ("description", ckeditor.fields.RichTextField(blank=True)),
                        (
                            "image",
                            cloudinary.models.CloudinaryField(
                                blank=True,
                                max_length=255,
                                null=True,
                                verbose_name="about_us_image",
                            ),
                        ),
                        (
                            "journey_title",
                            models.CharField(
                                blank=True, default="Our Journey", max_length=200
                            ),
                        ),
                        (
                            "journey_subtitle",
                            models.CharField(
                                blank=True,
                                default="From humble beginnings to a leading healthcare institution",
                                max_length=300,
                            ),
                        ),
                        (
                            "journey_description",
                            ckeditor.fields.RichTextField(blank=True),
                        ),
                        ("updated_at", models.DateTimeField(auto_now=True)),
                    ],
                    options={
                        "db_table": "core_aboutus",
                        "verbose_name": "About Us",
                        "verbose_name_plural": "About Us",
                    },
                ),
                migrations.CreateModel(
                    name="Milestone",
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
                        ("year", models.CharField(max_length=20)),
                        ("event", models.TextField()),
                        (
                            "about_us",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE,
                                related_name="milestones",
                                to="aboutus.aboutus",
                            ),
                        ),
                    ],
                    options={"db_table": "core_milestone"},
                ),
                migrations.CreateModel(
                    name="Leader",
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
                        ("role", models.CharField(max_length=100)),
                        (
                            "image",
                            cloudinary.models.CloudinaryField(
                                blank=True,
                                max_length=255,
                                null=True,
                                verbose_name="leader_image",
                            ),
                        ),
                        (
                            "nmc_number",
                            models.CharField(blank=True, max_length=50, null=True),
                        ),
                        ("description", ckeditor.fields.RichTextField(blank=True)),
                        (
                            "about_us",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE,
                                related_name="leaders",
                                to="aboutus.aboutus",
                            ),
                        ),
                    ],
                    options={"db_table": "core_leader"},
                ),
            ],
        ),
    ]
