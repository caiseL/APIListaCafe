# Generated by Django 3.2.1 on 2021-05-04 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receta',
            old_name='ingredientes',
            new_name='campo_receta',
        ),
        migrations.RenameField(
            model_name='receta',
            old_name='personas',
            new_name='numero_personas',
        ),
    ]
