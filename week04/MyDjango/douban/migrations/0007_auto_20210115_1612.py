# Generated by Django 2.2.13 on 2021-01-15 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('douban', '0006_auto_20210115_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]