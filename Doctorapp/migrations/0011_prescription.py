# Generated by Django 3.0.2 on 2020-02-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctorapp', '0010_delete_prescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appid', models.IntegerField()),
                ('docid', models.IntegerField()),
                ('pid', models.IntegerField()),
                ('Medicine', models.CharField(max_length=50)),
                ('Dosage', models.IntegerField()),
                ('Nod', models.IntegerField()),
            ],
        ),
    ]