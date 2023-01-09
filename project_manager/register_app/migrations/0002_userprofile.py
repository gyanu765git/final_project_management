# Generated by Django 4.1.5 on 2023-01-09 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_management_app', '__first__'),
        ('register_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='base_app/static/img/avatar/blank_profile.png', upload_to='base_app/static/img/avatar')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register_app.company')),
                ('project', models.ManyToManyField(blank=True, to='project_management_app.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
