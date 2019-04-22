# Generated by Django 2.0.3 on 2019-04-22 12:57

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0003_auto_20190419_2337'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fundlog',
            options={'verbose_name': '基金净值记录', 'verbose_name_plural': '基金净值记录'},
        ),
        migrations.AddField(
            model_name='fundlog',
            name='date',
            field=models.DateField(default=utils.local_date, verbose_name='日期'),
        ),
        migrations.AddField(
            model_name='investmentlog',
            name='date',
            field=models.DateField(default=utils.local_date, verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='fundlog',
            name='value',
            field=models.FloatField(default=0, verbose_name='净值'),
        ),
    ]
