# Generated by Django 2.0.3 on 2019-04-19 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最近更新时间')),
                ('value', models.FloatField(default=0, verbose_name='估值')),
            ],
            options={
                'verbose_name': '基金估值记录',
                'verbose_name_plural': '基金估值记录',
            },
        ),
        migrations.CreateModel(
            name='InvestmentLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最近更新时间')),
                ('quantity', models.IntegerField(default=0, verbose_name='投入/卖出份额')),
            ],
            options={
                'verbose_name': '投入卖出记录',
                'verbose_name_plural': '投入卖出记录',
            },
        ),
        migrations.AlterField(
            model_name='fund',
            name='code',
            field=models.CharField(db_index=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='fund',
            name='name',
            field=models.CharField(db_index=True, max_length=32),
        ),
        migrations.AddField(
            model_name='investmentlog',
            name='fund',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funds.Fund'),
        ),
    ]
