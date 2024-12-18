# Generated by Django 5.1.4 on 2024-12-12 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorprofile',
            name='shift_schedule',
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='specialties',
            field=models.ManyToManyField(blank=True, to='Doctors.specialty'),
        ),
    ]
