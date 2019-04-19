from django.db import models

class Fund(models.Model):

    name = models.CharField(max_length=32)
    code = models.CharField(max_length=32)
    brief = models.CharField(max_length=128)
    type = models.CharField(max_length=12)

    class Meta:
        verbose_name = '基金'
        verbose_name_plural = '基金'
