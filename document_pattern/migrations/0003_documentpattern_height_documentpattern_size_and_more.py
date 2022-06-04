# Generated by Django 4.0.4 on 2022-06-03 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_pattern', '0002_rename_accepted_types_documentpattern_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentpattern',
            name='height',
            field=models.IntegerField(default=3000),
        ),
        migrations.AddField(
            model_name='documentpattern',
            name='size',
            field=models.IntegerField(default=16),
        ),
        migrations.AddField(
            model_name='documentpattern',
            name='width',
            field=models.IntegerField(default=3000),
        ),
    ]
