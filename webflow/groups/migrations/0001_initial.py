# Generated by Django 4.2.5 on 2023-09-16 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0005_user_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Title')),
                ('formed', models.CharField(max_length=50, verbose_name='Group Formed')),
                ('img', models.ImageField(upload_to='group/card', verbose_name='Card Image')),
                ('img2', models.ImageField(upload_to='group/banner', verbose_name='banner Image')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profiles', verbose_name='Leader')),
            ],
        ),
    ]
