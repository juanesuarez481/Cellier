# Generated by Django 4.1.6 on 2023-02-14 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantries', '0003_recipe_difficulty_alter_recipe_preparation_time_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='quantity_unit',
            field=models.CharField(choices=[('Grams', 'Grams'), ('Kilograms', 'Kilograms'), ('Unit', 'Unit'), ('Spoon', 'Spoon'), ('Piece', 'Piece')], default='Kilograms', max_length=10),
        ),
    ]