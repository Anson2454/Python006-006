# Generated by Django 2.2.13 on 2021-01-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('douban', '0003_auto_20210115_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.CharField(max_length=5, verbose_name='评分'),
        ),
    ]
