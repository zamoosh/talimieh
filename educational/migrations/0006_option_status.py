# Generated by Django 4.0.2 on 2022-04-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational', '0005_alter_degreefieldstudy_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
