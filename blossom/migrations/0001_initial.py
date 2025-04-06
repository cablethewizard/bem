# Generated by Django 5.2 on 2025-04-06 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('startdate', models.DateField(null=True, verbose_name='Start Date')),
                ('enddate', models.DateField(null=True, verbose_name='End Date')),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('eventlocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blossom.show')),
            ],
        ),
        migrations.CreateModel(
            name='ShowEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('starttime', models.TimeField(null=True, verbose_name='Start Time')),
                ('endtime', models.TimeField(null=True, verbose_name='End Time')),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField(verbose_name='Event Date')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blossom.location')),
                ('show', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blossom.show')),
            ],
        ),
    ]
