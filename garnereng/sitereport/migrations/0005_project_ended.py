# Generated by Django 2.1.3 on 2018-11-19 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitereport', '0004_auto_20181118_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ended',
            field=models.DateField(blank=True, null=True),
        ),
    ]
