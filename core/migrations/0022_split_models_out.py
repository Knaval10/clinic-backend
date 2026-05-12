from django.db import migrations


class Migration(migrations.Migration):
    """State-only migration that removes the model definitions from the ``core`` app.

    The data and tables remain untouched (kept under ``core_*`` table names) and are
    re-attached to their new dedicated apps via ``SeparateDatabaseAndState`` migrations
    in each feature app.
    """

    dependencies = [
        ("core", "0021_remove_doctor_is_leadership_and_more"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.DeleteModel(name="Milestone"),
                migrations.DeleteModel(name="Leader"),
                migrations.DeleteModel(name="AboutUs"),
                migrations.DeleteModel(name="ContactMessage"),
                migrations.DeleteModel(name="Testimonial"),
                migrations.DeleteModel(name="Service"),
                migrations.DeleteModel(name="Doctor"),
                migrations.DeleteModel(name="HomePage"),
            ],
        ),
    ]
