# Generated by Django 3.1 on 2020-09-13 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_shelf', '0032_auto_20200913_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='can_create',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='can_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='can_manage_readers',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='can_manage_self',
            field=models.BooleanField(default=True),
        ),
    ]
