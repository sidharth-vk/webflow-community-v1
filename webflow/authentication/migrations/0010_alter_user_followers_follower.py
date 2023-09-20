# Generated by Django 4.2.5 on 2023-09-17 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_user_followers_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_followers',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profiles', verbose_name='Profile'),
        ),
    ]
