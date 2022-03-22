# Generated by Django 4.0.2 on 2022-03-21 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational', '0009_remove_educationalrequest_request_expert_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ownerdocument',
            options={},
        ),
        migrations.AlterField(
            model_name='educationalrequest',
            name='step',
            field=models.CharField(choices=[(1, 'must be approved by a register expert'), (2, 'must be approved by a financial expert'), (3, 'must be approved by an educational expert')], default=(1, 'must be approved by a register expert'), max_length=1),
        ),
    ]
