# Generated by Django 2.2 on 2020-06-28 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pronunciation', '0007_auto_20200626_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audioalteration',
            name='updated_transcript',
        ),
    ]
