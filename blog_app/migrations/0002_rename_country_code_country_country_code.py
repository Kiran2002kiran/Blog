# Generated by Django 5.1.4 on 2024-12-30 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='Country_code',
            new_name='country_code',
        ),
    ]
