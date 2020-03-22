# Generated by Django 2.2 on 2020-03-21 03:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_articulo_imagenrefencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='descuento',
            field=models.FloatField(default=0.00),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articulo',
            name='precio',
            field=models.FloatField(default=0.00),
            preserve_default=False,
        ),
    ]
