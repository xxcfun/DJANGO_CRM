from django.contrib import admin

# Register your models here.
from customer.models import Customer, Nature, Industry


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'website', 'scale', 'nature', 'industry', 'remarks', 'created_at', 'user', 'is_valid')
    fields = ('name', 'rank', 'website', 'scale', 'nature', 'industry', 'remarks', 'is_valid',
              'shop_province', 'shop_city', 'shop_area', 'shop_town', 'shop_address', 'shop_username', 'shop_phone',
              'invoice_province', 'invoice_city', 'invoice_area', 'invoice_town', 'invoice_address', 'invoice_username', 'invoice_phone')
    list_per_page = 10
    # date_hierarchy = 'created_at'
    ordering = ['-created_at']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(CustomerAdmin, self).save_model(request, obj, form, change)

    # def get_queryset(self, request):
    #     user = str(request.user)
    #     queryset = super(CustomerAdmin, self).get_queryset(request)
    #     if (user=='admin'):
    #         return queryset
    #     else:
    #         return queryset.filter(principal=request.user)


# @admin.register(CustomerShopAddress)
# class CustomerShopAddressAdmin(admin.ModelAdmin):
#     list_display = ('customer', 'province', 'city', 'address', 'username', 'phone', 'created_at', 'is_valid')
#     fields = ('customer', 'province', 'city', 'area', 'town', 'address', 'username', 'phone', 'is_valid')
#
#
# @admin.register(CustomerInvoiceAddress)
# class CustomerInvoiceAddressAdmin(admin.ModelAdmin):
#     list_display = ('customer', 'province', 'city', 'address', 'username', 'phone', 'created_at', 'is_valid')
#     fields = ('customer', 'province', 'city', 'area', 'town', 'address', 'username', 'phone', 'is_valid')


@admin.register(Nature)
class NatureAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 10


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 10
