# Generated by Django 3.0.7 on 2022-01-03 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20220103_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='is_features',
            new_name='is_featured',
        ),
    ]
