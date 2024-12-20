# Generated by Django 5.1.4 on 2024-12-17 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0002_trips'),
    ]

    operations = [
        migrations.AddField(
            model_name='trips',
            name='travelled_by',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.CASCADE, related_name='travelled_by', to='passenger.passenger'),
            preserve_default=False,
        ),
    ]
