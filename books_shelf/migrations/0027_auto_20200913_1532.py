# Generated by Django 3.1 on 2020-09-13 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_shelf', '0026_auto_20200913_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='rights',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='books_shelf.usertype'),
        ),
    ]
