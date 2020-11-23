import re

from django import forms

from customer.models import Customer
from liaison.models import Liaison


class LiaisonAddForm(forms.ModelForm):
    """联系人新增"""

    def __init__(self, request, customer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.fields['customer'].queryset = Customer.objects.filter(name=customer)

    class Meta:
        model = Liaison
        fields = ['name', 'customer', 'phone', 'job', 'injob',
                  'wx', 'qq', 'email', 'hobby', 'birthday', 'remarks']

    def clean_phone(self):
        """验证用户输入的手机号"""
        phone = self.cleaned_data['phone']
        # 判断用户名是否为手机号码
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, phone):
            raise forms.ValidationError('请输入正确的手机号码')
        return phone

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.user = self.request.user
        obj.save()


class LiaisonEditForm(forms.ModelForm):
    """联系人修改"""

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    class Meta:
        model = Liaison
        fields = ['name', 'customer', 'phone', 'job', 'injob',
                  'wx', 'qq', 'email', 'hobby', 'birthday', 'remarks']

    def clean_phone(self):
        """验证用户输入的手机号"""
        phone = self.cleaned_data['phone']
        # 判断用户名是否为手机号码
        pattern = r'^1[0-9]{10}$'
        if not re.search(pattern, phone):
            raise forms.ValidationError('请输入正确的手机号码')
        return phone

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.user = self.request.user
        obj.save()
