# Generated by Django 4.2 on 2024-12-12 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_feature_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='addition',
            name='icon',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
