# Generated by Django 3.0.2 on 2020-02-10 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doctorapp', '0014_auto_20200209_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medihis',
            old_name='Medication',
            new_name='Medicine',
        ),
    ]
