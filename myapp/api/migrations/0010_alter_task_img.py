# Generated by Django 5.1.4 on 2024-12-31 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_remove_task_photo_task_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to="photos/"),
        ),
    ]
