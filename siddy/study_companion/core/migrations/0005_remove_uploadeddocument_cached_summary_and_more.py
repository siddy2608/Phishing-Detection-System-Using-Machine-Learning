# Generated by Django 5.2.4 on 2025-07-21 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_uploadeddocument_cached_summary_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadeddocument',
            name='cached_summary',
        ),
        migrations.RemoveField(
            model_name='uploadeddocument',
            name='summary_generated_at',
        ),
    ]
