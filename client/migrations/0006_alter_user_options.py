# Generated by Django 4.0.2 on 2022-03-28 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('can_set_expert', 'can set expert'), ('normal_person', 'normal person')]},
        ),
    ]
