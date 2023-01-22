# Generated by Django 4.1.5 on 2023-01-22 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_management_app', '0004_alter_task_assign_alter_task_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assign',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
