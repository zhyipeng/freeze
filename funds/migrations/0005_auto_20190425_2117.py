# Generated by Django 2.0.3 on 2019-04-25 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0004_auto_20190422_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investmentlog',
            name='quantity',
        ),
        migrations.AddField(
            model_name='investmentlog',
            name='value',
            field=models.FloatField(default=0, verbose_name='投入/卖出金额'),
        ),
    ]
