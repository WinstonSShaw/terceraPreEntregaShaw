# Generated by Django 5.1.4 on 2024-12-13 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consola', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='fecha_inicio',
            field=models.DateField(null=True),
        ),
    ]
