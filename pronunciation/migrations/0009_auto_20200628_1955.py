# Generated by Django 2.2 on 2020-06-28 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pronunciation', '0008_remove_audioalteration_updated_transcript'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audioalteration',
            old_name='audio_url',
            new_name='relative_filename',
        ),
    ]