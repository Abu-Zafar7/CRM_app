# Generated by Django 4.2.6 on 2023-10-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('class_or_school', models.CharField(max_length=100)),
                ('tutor_name', models.CharField(max_length=100)),
                ('subjects', models.CharField(max_length=100)),
                ('starting_date', models.CharField(max_length=100)),
                ('fee', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('sr_no', models.PositiveIntegerField(blank=True, default=0, null=True, unique=True)),
            ],
        ),
    ]
