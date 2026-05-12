import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):
    """State-only migration: model previously lived in the ``core`` app.

    The corresponding ``core_homepage`` table already exists in the database
    (created by historical ``core`` migrations), so no DDL is executed here.
    """

    initial = True

    dependencies = [
        ("core", "0022_split_models_out"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.CreateModel(
                    name="HomePage",
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
                        ("subtitle", models.CharField(blank=True, max_length=300)),
                        ("description", models.TextField(blank=True)),
                        (
                            "banner_image",
                            cloudinary.models.CloudinaryField(
                                blank=True,
                                max_length=255,
                                null=True,
                                verbose_name="banner_image",
                            ),
                        ),
                        ("updated_at", models.DateTimeField(auto_now=True)),
                    ],
                    options={
                        "db_table": "core_homepage",
                        "verbose_name": "Home Page Slide",
                        "verbose_name_plural": "Home Page Slides",
                    },
                ),
            ],
        ),
    ]
