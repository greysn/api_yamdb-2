# Generated by Django 2.2.16 on 2022-11-01 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20221101_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default=1, max_length=2),
        ),
    ]
