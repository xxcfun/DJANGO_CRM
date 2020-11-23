from django import forms

from business.models import CustomerBusiness
from customer.models import Customer


class BusinessAddForm(forms.ModelForm):
    """商机新增"""
    class Meta:
        model = CustomerBusiness
        fields = ['name', 'customer', 'winning_rate', 'money', 'remarks', 'prod_name', 'prod_number', 'prod_price']

    def __init__(self, request, customer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.fields['customer'].queryset = Customer.objects.filter(name=customer)

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.user = self.request.user
        obj.save()


class BusinessEditForm(forms.ModelForm):
    """商机修改"""
    class Meta:
        model = CustomerBusiness
        fields = ['name', 'customer', 'winning_rate', 'money', 'remarks', 'prod_name', 'prod_number', 'prod_price']

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.user = self.request.user
        obj.save()
