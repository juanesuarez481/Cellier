# Generated by Django 4.1.6 on 2023-02-14 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantries', '0002_recipe_preparation_recipe_preparation_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Basic', max_length=12),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time_unit',
            field=models.CharField(choices=[('Seconds', 'Seconds'), ('Minutes', 'Minutes'), ('Hours', 'Hours'), ('Days', 'Days'), ('Weeks', 'Weeks')], default='Minutes', max_length=10),
        ),
    ]
