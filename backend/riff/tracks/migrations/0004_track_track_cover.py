# Generated by Django 5.1.1 on 2024-10-02 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0003_remove_track_track_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='track_cover',
            field=models.ImageField(null=True, upload_to='track_covers'),
        ),
    ]
