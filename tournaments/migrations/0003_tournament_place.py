# Generated by Django 5.0.4 on 2024-04-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_participant_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='place',
            field=models.CharField(default='CDMX', max_length=255),
            preserve_default=False,
        ),
    ]