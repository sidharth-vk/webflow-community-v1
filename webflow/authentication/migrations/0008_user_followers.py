# Generated by Django 4.2.5 on 2023-09-17 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_user_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='User')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profiles', verbose_name='Profile')),
            ],
        ),
    ]
