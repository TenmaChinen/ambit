# Generated by Django 4.0.6 on 2024-09-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Adulto'), (1, 'Joven'), (2, 'Bebé')], null=True, verbose_name='Edad'),
        ),
    ]
