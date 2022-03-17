# Generated by Django 4.0.2 on 2022-03-17 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('educational', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('seen', models.DateTimeField(auto_now=True, null=True)),
                ('user_seen', models.BooleanField(blank=True, default=False, null=True)),
                ('expert_seen', models.BooleanField(blank=True, default=False, null=True)),
                ('educational_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educational.educationalrequest')),
                ('massage_expert', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='massage_expert', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]