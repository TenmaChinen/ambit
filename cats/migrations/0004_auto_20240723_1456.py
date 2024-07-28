# Generated by Django 3.2.6 on 2024-07-23 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0001_initial'),
        ('cats', '0003_alter_cat_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='disease',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='diseases.disease', verbose_name='Afecciones'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='frequency',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Habitual'), (1, 'Ocasional'), (2, 'Raramente')], default=0, null=True, verbose_name='Frecuencia de visita'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='sociability',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Sí'), (1, 'Ocasional'), (2, 'No')], default=1, null=True, verbose_name='Sociable'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='state',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Presente'), (1, 'Fallecido'), (2, 'Desaparecido'), (3, 'Adoptado')], default=0, null=True, verbose_name='Estado'),
        ),
    ]
