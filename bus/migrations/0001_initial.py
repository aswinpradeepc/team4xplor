# Generated by Django 5.1.4 on 2024-12-17 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Busstop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stopname', models.CharField(max_length=50)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('stop_id', models.CharField(editable=False, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare_matrix', models.JSONField()),
                ('route_id', models.CharField(editable=False, max_length=20, unique=True)),
                ('first_stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_stops', to='bus.busstop')),
                ('last_stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_stops', to='bus.busstop')),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=30)),
                ('reg_no', models.CharField(max_length=20)),
                ('route_trip1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_trip1', to='bus.route')),
                ('route_trip2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_trip2', to='bus.route')),
                ('route_trip3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_trip3', to='bus.route')),
            ],
        ),
    ]
