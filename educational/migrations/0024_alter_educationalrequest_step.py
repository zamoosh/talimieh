# Generated by Django 4.0.2 on 2022-03-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational', '0023_alter_educationalrequest_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationalrequest',
            name='step',
            field=models.CharField(choices=[(1, 'must be approved by a register expert'), (2, 'must be approved by an educational expert'), (3, 'must be approved by a financial expert'), (4, 'must be re-approved by the educational expert'), (5, 'must be re-approved by the financial expert'), (6, 'educational expert must approved final submit'), (7, 'request is submitted'), (0, 'request is rejected')], default=(1, 'must be approved by a register expert'), max_length=1),
        ),
    ]