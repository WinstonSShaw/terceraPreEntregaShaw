# Generated by Django 5.1.4 on 2024-12-13 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consola', '0002_juego_fecha_inicio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='juego',
            old_name='nombre',
            new_name='nombre_juego',
        ),
    ]
