# Generated by Django 4.2.5 on 2023-09-17 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0006_group_about_alter_grp_feed_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='grp_talks_about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Talks About')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group', verbose_name='Group')),
            ],
        ),
        migrations.CreateModel(
            name='grp_skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech', models.CharField(max_length=250, verbose_name='Technology')),
                ('image', models.ImageField(upload_to='user/skill', verbose_name='Logo ')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group', verbose_name='Group')),
            ],
        ),
    ]
