# Generated by Django 4.2.1 on 2023-05-30 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_delete_project_remove_service_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about_us',
            name='image_thumbnail',
        ),
    ]
