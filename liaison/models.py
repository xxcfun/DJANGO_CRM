from django.db import models

# Create your models here.
from users.models import User
from customer.models import Customer
from utils import constants


class Liaison(models.Model):
    """联系人模型"""
    customer = models.ForeignKey(Customer, related_name='liaison')
    name = models.CharField('联系人姓名', max_length=64)
    phone = models.CharField('联系人电话', max_length=11)
    job = models.SmallIntegerField('职称', choices=constants.JOB_ITEMS, default=constants.JOB_BUSINESS)
    injob = models.SmallIntegerField('是否在职', choices=constants.INJOB_ITEMS, default=constants.INJOB_YES)

    wx = models.CharField('微信', max_length=64, blank=True, null=True)
    qq = models.CharField('QQ', max_length=64, blank=True, null=True)
    email = models.EmailField('电子邮箱', max_length=64, blank=True, null=True)
    hobby = models.CharField('兴趣爱好', max_length=128, blank=True, null=True)
    birthday = models.CharField('生日', max_length=64, blank=True, null=True)
    remarks = models.CharField('联系人备注', max_length=255, blank=True, null=True)

    user = models.ForeignKey(User, verbose_name='创建人', related_name='liaison')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)
    is_valid = models.BooleanField('是否有效', default=True)

    class Meta:
        db_table = 'liaison'
        verbose_name = verbose_name_plural = "联系人"

    def __str__(self):
        return self.name
