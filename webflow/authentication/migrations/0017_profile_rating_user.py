# Generated by Django 4.2.5 on 2023-09-17 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0016_profile_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_rating',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.profiles', verbose_name='Name'),
            preserve_default=False,
        ),
    ]
