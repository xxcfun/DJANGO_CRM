from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from customer.models import Customer
from utils import constants


class Product(models.Model):
    name = models.CharField('货品名称', max_length=64)
    number = models.IntegerField('数量')
    price = models.FloatField('价格', max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bus_product'
        verbose_name = verbose_name_plural = '商机产品'


class CustomerBusiness(models.Model):
    """客户商机"""
    name = models.CharField('商机名称', max_length=64)
    customer = models.ForeignKey(Customer, verbose_name='商机客户')
    winning_rate = models.SmallIntegerField('赢单率', choices=constants.WINNING_ITEMS, default=constants.WINNING_ERSHI)
    money = models.CharField('预估金额', max_length=16, blank=True, null=True)
    remarks = models.CharField('商机备注', max_length=255, blank=True, null=True)

    user = models.ForeignKey(User, verbose_name='创建人', related_name='customer_business')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)
    is_valid = models.BooleanField('是否有效', default=True)

    prod_name = models.CharField('货品名称', max_length=64, blank=True, null=True)
    prod_number = models.IntegerField('数量', blank=True, null=True)
    prod_price = models.FloatField('价格', max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'business'
        verbose_name = verbose_name_plural = "客户商机"

    def __str__(self):
        return self.name
