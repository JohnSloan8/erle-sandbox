# Generated by Django 2.2 on 2020-06-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pronunciation', '0006_auto_20200626_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='audioalteration',
            name='transcript_added',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='audioalteration',
            name='transcript_deleted',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='audioalteration',
            name='updated_words',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]