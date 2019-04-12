# Generated by Django 2.2 on 2019-04-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20190411_1242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.TextField(blank=True, verbose_name='Sobre o curso'),
        ),
    ]