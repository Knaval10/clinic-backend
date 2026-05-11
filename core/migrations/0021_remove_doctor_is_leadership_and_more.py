from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_doctor_options_doctor_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='is_leadership',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='leadership_role',
        ),
    ]
