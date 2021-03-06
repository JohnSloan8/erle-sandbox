# Generated by Django 2.2 on 2020-06-26 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pronunciation', '0005_typedalteration'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioAlteration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_transcript', models.CharField(blank=True, max_length=500, null=True)),
                ('updated_words', models.CharField(blank=True, max_length=500, null=True)),
                ('audio_url', models.CharField(blank=True, max_length=200, null=True)),
                ('visemes', models.CharField(blank=True, max_length=4000, null=True)),
                ('audio_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pronunciation.AudioFile')),
            ],
        ),
        migrations.DeleteModel(
            name='TypedAlteration',
        ),
    ]
