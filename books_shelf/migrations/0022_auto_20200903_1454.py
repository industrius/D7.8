# Generated by Django 3.1 on 2020-09-03 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_shelf', '0021_auto_20200902_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='full_name',
            field=models.CharField(max_length=100, verbose_name='Имя друга'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Наименование издательства'),
        ),
    ]
