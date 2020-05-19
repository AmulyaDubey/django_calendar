# Generated by Django 3.0.6 on 2020-05-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_auto_20200519_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(db_column='title', max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(db_column='email', max_length=150, null=True, unique=True),
        ),
    ]
