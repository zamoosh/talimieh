# Generated by Django 4.0.2 on 2022-03-19 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational', '0006_alter_educationalrequest_step'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationalrequest',
            name='educational_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='educationalrequest',
            name='financial_status',
            field=models.BooleanField(default=False),
        ),
    ]
