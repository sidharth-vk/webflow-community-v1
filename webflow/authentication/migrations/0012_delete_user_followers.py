# Generated by Django 4.2.5 on 2023-09-17 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_user_follow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_followers',
        ),
    ]