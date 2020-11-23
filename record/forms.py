from django import forms

from customer.models import Customer
from record.models import CustomerRecord


class RecordAddForm(forms.ModelForm):
    """拜访记录新增"""

    def __init__(self, request, customer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.fields['customer'].queryset = Customer.objects.filter(name=customer)

    class Meta:
        model = CustomerRecord
        fields = ['customer', 'status', 'main', 'next', 'remarks']

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.user = self.request.user
        obj.save()


class RecordEditForm(forms.ModelForm):
    """拜访记录修改"""

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    class Meta:
        model = CustomerRecord
        fields = ['customer', 'status', 'main', 'next', 'remarks']

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.user = self.request.user
        obj.save()
