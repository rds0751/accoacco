# Generated by Django 2.2.13 on 2021-08-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0006_expensetransaction_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensetransaction',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
