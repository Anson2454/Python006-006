# Generated by Django 2.2.13 on 2021-01-15 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('douban', '0004_auto_20210115_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='movie_name',
            field=models.CharField(max_length=50, verbose_name='电影名'),
        ),
    ]
