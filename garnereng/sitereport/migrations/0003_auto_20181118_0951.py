# Generated by Django 2.1.3 on 2018-11-18 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitereport', '0002_auto_20181118_0850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='decider',
        ),
        migrations.RemoveField(
            model_name='client',
            name='lead',
        ),
        migrations.AddField(
            model_name='project',
            name='decider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='decision_maker', to='sitereport.Person'),
        ),
        migrations.AddField(
            model_name='project',
            name='lead',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_lead', to='sitereport.Person'),
        ),
    ]
