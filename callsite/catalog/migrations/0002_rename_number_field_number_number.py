# Generated by Django 5.0.1 on 2024-01-24 16:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="number",
            old_name="number_field",
            new_name="number",
        ),
    ]
