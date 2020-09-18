# Generated by Django 3.1 on 2020-09-13 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_shelf', '0030_auto_20200913_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='rights',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='books_shelf.usertype'),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='title',
            field=models.CharField(default=0, max_length=25, verbose_name='Роль'),
        ),
    ]