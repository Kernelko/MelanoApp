# Generated by Django 2.0.3 on 2018-04-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0005_remove_picture_file_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture_file',
            name='is_cancer',
            field=models.BooleanField(default=False),
        ),
    ]