# Generated by Django 2.1.5 on 2022-05-21 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0007_auto_20181229_1401'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.AlterModelOptions(
            name='meals',
            options={'verbose_name': 'platillo', 'verbose_name_plural': 'platillos'},
        ),
    ]