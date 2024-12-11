# Generated by Django 5.1.4 on 2024-12-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(default='guest', max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('role', models.CharField(choices=[('Patient', 'Patient'), ('Doctor', 'Doctor'), ('Nurse', 'Nurse'), ('Staff', 'Administrative Staff'), ('Admin', 'Hospital Administrator')], max_length=50)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]