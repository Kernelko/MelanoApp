# Generated by Django 2.0.3 on 2018-04-25 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0006_auto_20180420_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='current_pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
