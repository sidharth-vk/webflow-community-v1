# Generated by Django 4.2.5 on 2023-09-18 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_event_category_events_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_category',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
