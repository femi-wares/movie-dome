# Generated by Django 5.1.1 on 2024-11-15 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedomeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='related',
            name='movies_relationship',
        ),
        migrations.RemoveField(
            model_name='related',
            name='series_relationship',
        ),
        migrations.AddField(
            model_name='related',
            name='movies_relationship',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='moviedomeapp.movies'),
        ),
        migrations.AddField(
            model_name='related',
            name='series_relationship',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='moviedomeapp.series'),
        ),
    ]
