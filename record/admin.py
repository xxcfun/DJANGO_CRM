from django.contrib import admin

# Register your models here.


# 状态
from record.models import Status, CustomerRecord


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']


# 拜访记录
@admin.register(CustomerRecord)
class CustomerRecordAdmin(admin.ModelAdmin):
    list_display = ['customer', 'status', 'main', 'next', 'remarks', 'created_at', 'is_valid', 'user']
    fields = ['customer', 'status', 'main', 'next', 'remarks', 'is_valid']
    list_per_page = 10
    ordering = ['-created_at']
    # list_filter = [CustomerRecordOwnerFilter, 'status']
    search_fields = ['customer', 'customer__name']
    actions_on_top = True
    actions_on_bottom = True

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(CustomerRecordAdmin, self).save_model(request, obj, form, change)
