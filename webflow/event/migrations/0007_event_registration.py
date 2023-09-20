# Generated by Django 4.2.5 on 2023-09-18 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0020_user_education_college_alter_user_education_course'),
        ('event', '0006_event_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='event_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50, verbose_name='Team')),
                ('college', models.CharField(max_length=250, verbose_name='College Name')),
                ('semester', models.CharField(max_length=50, verbose_name='Semester')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profiles', verbose_name='Profile - User')),
            ],
        ),
    ]
