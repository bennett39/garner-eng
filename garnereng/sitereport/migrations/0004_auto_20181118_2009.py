# Generated by Django 2.1.3 on 2018-11-19 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitereport', '0003_auto_20181118_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='contractor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contractor_projects', to='sitereport.Contractor'),
        ),
    ]