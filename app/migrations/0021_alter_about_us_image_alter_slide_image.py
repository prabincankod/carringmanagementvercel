# Generated by Django 4.1.6 on 2023-05-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_about_us_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_us',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='carousel'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to='carousel'),
        ),
    ]
