# Generated by Django 3.2.5 on 2021-07-15 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cal_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.TextField()),
                ('reward', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DailyPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what', models.TextField()),
                ('when', models.TimeField()),
                ('day_assigned', models.DateField()),
                ('who', models.TextField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cal_app.goal')),
            ],
        ),
    ]
