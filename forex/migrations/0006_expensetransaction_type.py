# Generated by Django 2.2.13 on 2021-08-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0005_auto_20210827_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensetransaction',
            name='type',
            field=models.CharField(blank=True, choices=[('cheque', 'cheque'), ('credit', 'credit'), ('debit', 'debit')], max_length=32, null=True),
        ),
    ]