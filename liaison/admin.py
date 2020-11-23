from django.contrib import admin

# Register your models here.


# 联系人
from liaison.models import Liaison


@admin.register(Liaison)
class LiaisonAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'customer', 'job', 'injob',
                    'wx', 'qq', 'email', 'hobby', 'birthday',
                    'remarks', 'created_at', 'is_valid', 'user']
    fields = ['name', 'phone', 'customer', 'job', 'injob',
              'wx', 'qq', 'email', 'hobby', 'birthday',
              'remarks', 'is_valid']
    list_per_page = 10
    ordering = ['-created_at']
    # list_filter = [LiaisonOwnerFilter]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(LiaisonAdmin, self).save_model(request, obj, form, change)
