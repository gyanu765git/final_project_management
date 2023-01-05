# Generated by Django 4.1.5 on 2023-01-03 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management_app', '0003_alter_project_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='assign',
        ),
        migrations.AlterField(
            model_name='project',
            name='expected_start_date',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='project',
            name='assign',
            field=models.CharField(default=1, max_length=80),
        ),
    ]
