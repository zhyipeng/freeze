from django.db import models

from core.models import BaseModelWithTimeField
from utils import local_date


class Fund(models.Model):

    name = models.CharField(max_length=32, db_index=True)
    code = models.CharField(max_length=32, db_index=True)
    brief = models.CharField(max_length=128)
    type = models.CharField(max_length=12)

    class Meta:
        verbose_name = '基金'
        verbose_name_plural = '基金'


class FundLog(BaseModelWithTimeField):

    fund = models.ForeignKey(Fund, on_delete=models.CASCADE)
    value = models.FloatField('净值', default=0)
    date = models.DateField('日期', default=local_date)

    class Meta:
        verbose_name = '基金净值记录'
        verbose_name_plural = '基金净值记录'


class InvestmentLog(BaseModelWithTimeField):

    fund = models.ForeignKey(Fund, on_delete=models.CASCADE)
    user = models.ForeignKey('members.User', on_delete=models.CASCADE)
    quantity = models.IntegerField('投入/卖出份额', default=0)
    date = models.DateField('日期', default=local_date)

    class Meta:
        verbose_name = '投入卖出记录'
        verbose_name_plural = '投入卖出记录'
