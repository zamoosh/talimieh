# Generated by Django 4.0.2 on 2022-03-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational', '0020_alter_educationalrequest_step'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationalrequest',
            name='educational_status_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='educationalrequest',
            name='financial_status_2',
            field=models.BooleanField(default=False),
        ),
    ]