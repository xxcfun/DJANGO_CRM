from django.db import models

# Create your models here.
from utils import constants


class User(models.Model):
    """用户"""
    name = models.CharField('用户名', max_length=128, unique=True)
    password = models.CharField('密码', max_length=256)
    is_valid = models.BooleanField('是否有效', default=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    power = models.SmallIntegerField('权限', choices=constants.USER_ROLE, default=constants.ROLE_YW)

    class Meta:
        ordering = ['-created_time']
        verbose_name_plural = verbose_name = '用户'
        db_table = 'user'

    def __str__(self):
        return self.name


class Count(models.Model):
    """用户更新数据汇总表"""
    user = models.ForeignKey(User, related_name='count')
    add_cus = models.IntegerField('每日增加客户数', default=0)
    add_lia = models.IntegerField('每日增加联系人数', default=0)
    add_bus = models.IntegerField('每日增加商机数', default=0)
    add_rec = models.IntegerField('每日增加拜访记录数', default=0)

    class Meta:
        db_table = 'user_counts'
        verbose_name = verbose_name_plural = '数据汇总'

    def __str__(self):
        return self.user
