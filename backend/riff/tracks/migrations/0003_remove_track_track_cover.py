# Generated by Django 5.1.1 on 2024-09-29 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_alter_track_track_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='track_cover',
        ),
    ]
