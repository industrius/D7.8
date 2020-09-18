# Generated by Django 3.1 on 2020-09-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_shelf', '0037_auto_20200916_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='profile',
            field=models.ManyToManyField(blank=True, related_name='reader', to='books_shelf.Profile', verbose_name='Читатель'),
        ),
    ]
