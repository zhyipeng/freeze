from django.db import models
from django.db.models import Q
from jsonfield import JSONField

from core.models import BaseModelWithTimeField
from utils import hash256


class User(models.Model):

    nick_name = models.CharField(max_length=32, unique=True)
    mobile = models.CharField(max_length=12, default='')
    password = models.CharField(max_length=256)
    concerned_funds = JSONField('关注的基金代码', default=list)

    class Meta:
        unique_together = ['nick_name', 'mobile']

    @classmethod
    def login(cls, password, username):
        password = hash256(password)
        user = User.objects.filter(
            Q(nick_name=username) | Q(mobile=username),
            password=password).first()

        return user


class UserFund(BaseModelWithTimeField):

    fund = models.ForeignKey('funds.Fund', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('持有份额', default=0)

    class Meta:
        verbose_name = '用户持有基金'
        verbose_name_plural = '用户持有基金'
