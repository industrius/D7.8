# Generated by Django 3.1 on 2020-08-31 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_shelf', '0018_auto_20200830_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='', upload_to='img/', verbose_name='Изображение'),
        ),
    ]
