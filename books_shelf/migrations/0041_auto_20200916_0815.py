# Generated by Django 3.1 on 2020-09-16 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_shelf', '0040_auto_20200916_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='readers',
            field=models.ManyToManyField(blank=True, related_name='rented_books', to='books_shelf.Profile', verbose_name='Читатели'),
        ),
    ]