# Generated by Django 2.2.13 on 2021-09-07 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0011_auto_20210903_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensetransaction',
            name='value1',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Value USD'),
        ),
        migrations.AlterField(
            model_name='expensetransaction',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Value INR'),
        ),
    ]
