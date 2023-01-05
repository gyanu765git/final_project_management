# Generated by Django 4.1.5 on 2023-01-03 07:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_management_app', '0004_remove_project_assign_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='assign',
        ),
        migrations.AddField(
            model_name='project',
            name='assign',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
