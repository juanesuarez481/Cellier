# Generated by Django 4.1.6 on 2023-02-14 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pantries', '0006_alter_ingredient_quantity_unit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['difficulty']},
        ),
    ]