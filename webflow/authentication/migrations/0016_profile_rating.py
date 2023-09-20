# Generated by Django 4.2.5 on 2023-09-17 17:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_remove_user_skills_image_remove_user_skills_tech_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('email', models.CharField(max_length=250, verbose_name='Email')),
                ('comment', ckeditor.fields.RichTextField()),
                ('rating', models.CharField(max_length=50, verbose_name='Rating')),
            ],
        ),
    ]
