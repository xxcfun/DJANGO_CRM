from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Count(models.Model):
    """用户更新数据汇总表"""
    user = models.ForeignKey(User, related_name='count')
    add_cus = models.IntegerField('每日增加客户数', default=0)
    add_lia = models.IntegerField('每日增加联系人数', default=0)
    add_bus = models.IntegerField('每日增加商机数', default=0)
    add_rec = models.IntegerField('每日增加拜访记录数', default=0)

    class Meta:
        db_table = 'counts'
        verbose_name = verbose_name_plural = '数据汇总'

    def __str__(self):
        return self.user
