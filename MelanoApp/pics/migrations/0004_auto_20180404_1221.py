# Generated by Django 2.0.3 on 2018-04-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0003_picture_file_is_cancer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture_file',
            name='is_cancer',
            field=models.BooleanField(default=True),
        ),
    ]
