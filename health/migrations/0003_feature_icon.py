# Generated by Django 4.2 on 2024-12-12 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='icon',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
