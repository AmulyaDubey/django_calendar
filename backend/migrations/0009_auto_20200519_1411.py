# Generated by Django 3.0.6 on 2020-05-19 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20200519_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(db_column='email', max_length=150),
        ),
    ]
