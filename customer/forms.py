import re

from django import forms

from customer.models import Customer
from users.models import Count


class CustomerForm(forms.ModelForm):
    """客户新增/修改"""
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    class Meta:
        model = Customer
        fields = ['name', 'rank', 'website', 'scale', 'nature', 'industry', 'remarks',
                  'shop_province', 'shop_city', 'shop_area', 'shop_town', 'shop_address', 'shop_username', 'shop_phone',
                  'invoice_province', 'invoice_city', 'invoice_area', 'invoice_town', 'invoice_address', 'invoice_username', 'invoice_phone',
                  ]

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.user = self.request.user
        obj.save()


class CountForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super(CountForm, self).__init__(*args, **kwargs)
        self.request = request

    class Meta:
        model = Count
        fields = ['user', 'add_cus', 'add_lia', 'add_bus', 'add_rec']

    def save(self, commit=True):
        obj = super().save(commit=True)
        obj.user = self.request.user
        obj.save()
# class ShopForm(forms.ModelForm):
#     """收货地址"""
#     def __init__(self, request, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.request = request
#
#     class Meta:
#         model = CustomerShopAddress
#         fields = ['username', 'phone', 'province', 'city', 'area', 'address']
#
#     def save(self, commit=True):
#         obj = super().save(commit=False)
#         obj.user = self.request.user
#         obj.save()
#
#
# class InvoiceForm(forms.ModelForm):
#     """收货地址"""
#     def __init__(self, request, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.request = request
#
#     class Meta:
#         model = CustomerShopAddress
#         fields = ['username', 'phone', 'province', 'city', 'area', 'address']
#
#     def save(self, commit=True):
#         obj = super().save(commit=False)
#         obj.user = self.request.user
#         obj.save()
#
#
# class CustomerShopAddressForm(forms.ModelForm):
#     """收货地址新增|修改"""
#     region = forms.CharField(label='大区域选项', max_length=64, required=True,
#                              error_messages={
#                                  'required': '请选择地址'
#                              })
#
#     def __init__(self, request, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.request = request
#
#     class Meta:
#         model = CustomerShopAddress
#         fields = ['address', 'username', 'phone']
#
#     def clean_phone(self):
#         """验证手机号"""
#         phone = self.cleaned_data['phone']
#         pattern = r'^1[0-9]{10}$'
#         if not re.search(pattern, phone):
#             raise forms.ValidationError('请输入正确的手机号码')
#         return phone
#
#     def save(self, commit=True):
#         obj = super().save(commit=False)
#         region = self.cleaned_data['region']
#         (province, city, area) = region.split(' ')
#         obj.province = province
#         obj.city = city
#         obj.area = area
#         obj.user = self.request.user
#         obj.save()
#
#
# class CustomerInvoiceAddressForm(forms.ModelForm):
#     """收货地址新增|修改"""
#     region = forms.CharField(label='大区域选项', max_length=64, required=True,
#                              error_messages={
#                                  'required': '请选择地址'
#                              })
#
#     def __init__(self, request, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.request = request
#
#     class Meta:
#         model = CustomerInvoiceAddress
#         fields = ['address', 'username', 'phone']
#
#     def clean_phone(self):
#         """验证手机号"""
#         phone = self.cleaned_data['phone']
#         pattern = r'^1[0-9]{10}$'
#         if not re.search(pattern, phone):
#             raise forms.ValidationError('请输入正确的手机号码')
#         return phone
#
#     def save(self, commit=True):
#         obj = super().save(commit=False)
#         region = self.cleaned_data['region']
#         (province, city, area) = region.split(' ')
#         obj.province = province
#         obj.city = city
#         obj.area = area
#         obj.user = self.request.user
#         obj.save()