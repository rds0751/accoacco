# Generated by Django 2.2.13 on 2021-09-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0011_newexpensetransaction1'),
    ]

    operations = [
        migrations.AddField(
            model_name='newexpensetransaction1',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]