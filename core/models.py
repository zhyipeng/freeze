from django.db import models


class BaseModelWithTimeField(models.Model):
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, db_index=True)
    update_time = models.DateTimeField(verbose_name='最近更新时间', auto_now=True)

    class Meta:
        abstract = True
