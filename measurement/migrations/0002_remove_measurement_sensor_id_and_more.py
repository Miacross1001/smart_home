# Generated by Django 4.2.6 on 2023-10-17 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='sensor_id',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
