# Generated by Django 4.2.7 on 2024-06-10 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointmentmodel',
            options={'verbose_name': 'نوبت دهی سیگنال\u200cهای مغزی EEG'},
        ),
        migrations.AlterField(
            model_name='timesvisitmodel',
            name='time',
            field=models.CharField(max_length=30, verbose_name='ساعت نوبت دادن'),
        ),
        migrations.AlterField(
            model_name='weekstimemodel',
            name='weeks_time',
            field=models.CharField(max_length=10, verbose_name='روزهای هفته'),
        ),
        migrations.CreateModel(
            name='GetAppointmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('code_meli', models.CharField(max_length=12)),
                ('phone', models.CharField(max_length=12)),
                ('code_nobat', models.BigIntegerField()),
                ('time_visit', models.CharField(max_length=50)),
                ('create', models.DateTimeField(auto_now=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]