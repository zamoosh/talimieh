# Generated by Django 4.0.2 on 2022-03-12 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational', '0003_degreefieldstudy_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerdocument',
            name='image_status',
            field=models.BooleanField(default=True),
        ),
    ]
