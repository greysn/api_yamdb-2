# Generated by Django 3.0 on 2022-11-01 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='name',
            new_name='titles',
        ),
    ]
