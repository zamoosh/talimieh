# Generated by Django 4.0.6 on 2022-07-31 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document_pattern', '0003_documentpattern_types_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentpattern',
            name='document_type',
        ),
    ]
