# Generated by Django 4.2.5 on 2023-09-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_grp_feed'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='about',
            field=models.TextField(default=1, verbose_name='About'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grp_feed',
            name='img',
            field=models.ImageField(upload_to='group/feed', verbose_name='Image 660*450'),
        ),
    ]