# Generated by Django 2.2.13 on 2021-08-31 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erplogic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='slug',
            field=models.SlugField(blank=True, help_text='For fast recall', verbose_name='Identifier slug'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='slug',
            field=models.SlugField(blank=True, help_text='For fast recall', verbose_name='Identifier slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, help_text='For fast recall', verbose_name='Identifier slug'),
        ),
    ]
