# Generated by Django 4.0.4 on 2022-06-21 08:58

import client.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('cellphone', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('nationality', models.IntegerField(choices=[(0, 'arabic'), (1, 'afghanistan')], default=0)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=client.models.profile_image)),
                ('father_name', models.CharField(blank=True, max_length=15, null=True)),
                ('ancestor_name', models.CharField(blank=True, max_length=15, null=True)),
                ('nick_name', models.CharField(blank=True, max_length=15, null=True)),
                ('pass_number', models.CharField(blank=True, max_length=25, null=True)),
                ('birth_date', models.DateField(auto_now_add=True)),
                ('pass_issue_date', models.DateField(auto_now_add=True)),
                ('pass_expiration', models.DateField(auto_now_add=True)),
                ('place_birth', models.CharField(blank=True, max_length=15, null=True)),
                ('place_issue', models.CharField(blank=True, max_length=15, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=15, null=True)),
                ('first_login', models.BooleanField(default=True)),
                ('student_num', models.CharField(blank=True, max_length=10, null=True)),
                ('admin_create', models.BooleanField(default=False)),
                ('expert', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'permissions': [('can_set_expert', 'can set expert'), ('normal_person', 'normal person')],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
