# Generated by Django 4.2.6 on 2023-10-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_studentrecord_sr_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecord',
            name='sr_no',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, unique=True),
        ),
    ]
