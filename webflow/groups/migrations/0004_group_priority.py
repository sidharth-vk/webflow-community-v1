# Generated by Django 4.2.5 on 2023-09-17 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_grp_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='priority',
            field=models.IntegerField(default=1, verbose_name='priority'),
            preserve_default=False,
        ),
    ]
