# Generated by Django 3.0.2 on 2020-02-09 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctorapp', '0007_auto_20200209_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='docid',
            field=models.IntegerField(default=1),
        ),
    ]
