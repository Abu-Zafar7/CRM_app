# Generated by Django 4.2.6 on 2023-10-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_studentrecord_delete_studentrecords'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentrecord',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]