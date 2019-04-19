from django.db import models
from jsonfield import JSONField

from core.models import BaseModelWithTimeField


class User(models.Model):

    nick_name = models.CharField(max_length=32)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=256)
    concerned_funds = JSONField('关注的基金代码', default=list)


class UserFund(BaseModelWithTimeField):

    fund = models.ForeignKey('funds.Fund', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('持有份额', default=0)

    class Meta:
        verbose_name = '用户持有基金'
        verbose_name_plural = '用户持有基金'
