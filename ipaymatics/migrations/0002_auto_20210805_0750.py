# Generated by Django 2.2 on 2021-08-05 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipaymatics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='status',
            field=models.CharField(blank=True, choices=[('order_submitted', 'order_submitted'), ('completed', 'completed'), ('order_cancel', 'order_cancel')], max_length=32),
        ),
    ]
