# Generated by Django 3.0.6 on 2020-05-19 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20200519_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='id',
            new_name='post_id',
        ),
    ]
