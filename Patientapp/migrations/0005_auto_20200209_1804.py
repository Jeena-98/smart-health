# Generated by Django 3.0.2 on 2020-02-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patientapp', '0004_remove_patientreg_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Time',
            field=models.CharField(max_length=20),
        ),
    ]