# Generated by Django 3.2.5 on 2021-07-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
