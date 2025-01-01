# Generated by Django 5.1.4 on 2024-12-31 12:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_rename_country_code_country_country_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL),
        ),
    ]