# Generated by Django 4.2.5 on 2023-09-17 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_user_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_talsk_about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Talks About')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profiles', verbose_name='Profile - User')),
            ],
        ),
    ]
