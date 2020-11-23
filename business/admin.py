from django.contrib import admin
from business.models import CustomerBusiness
# Register your models here.


# 商机
@admin.register(CustomerBusiness)
class CustomerBusinessAdmin(admin.ModelAdmin):
    list_display = ['name', 'customer', 'winning_rate', 'money', 'remarks', 'created_at', 'is_valid', 'user']
    fields = ['name', 'customer', 'winning_rate', 'money', 'remarks', 'product', 'is_valid']
    ordering = ['-created_at']
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(CustomerBusinessAdmin, self).save_model(request, obj, form, change)
