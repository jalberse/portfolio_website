# Generated by Django 2.2.4 on 2019-08-13 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_gallery_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]