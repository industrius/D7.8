# Generated by Django 3.1 on 2020-08-19 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_shelf', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автора', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книгу', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='friend',
            options={'verbose_name': 'Друга', 'verbose_name_plural': 'Друзья'},
        ),
        migrations.AlterField(
            model_name='book',
            name='friend',
            field=models.ManyToManyField(blank=True, null=True, related_name='friend_took', to='books_shelf.Friend', verbose_name='Друг'),
        ),
    ]