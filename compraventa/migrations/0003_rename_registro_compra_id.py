# Generated by Django 4.0.4 on 2022-06-07 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compraventa', '0002_venta_delete_ventas_remove_cliente_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='registro',
            new_name='id',
        ),
    ]