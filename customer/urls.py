from django.conf.urls import url

from customer import views

urlpatterns = [
    # 查看客户
    url(r'^$', views.customer_list, name='customer_list'),
    # 根据筛选用户查看客户
    # url(r'^screen/$', views.customer_list, name='customer_list'),
    # 添加客户
    url(r'^add/$', views.customer_add, name='customer_add'),
    # 查看和修改客户
    url(r'^detail/(?P<pk>\d+)/$', views.customer_detail, name='customer_detail'),
    # 单个页面进行修改
    url(r'^edit/(?P<pk>\d+)/$', views.customer_edit, name='customer_edit'),
    # 删除客户
    url(r'^del/(?P<pk>\d+)/$', views.customer_delete, name='customer_delete'),
    # 导出
    # url(r'^export/$', views.export_excel, name='export_excel'),
    # # 收货地址的新增和修改
    # url(r'^shopadd/', views.shop_address_edit, name='shop_address_edit'),
    # # 发票地址的新增和修改
    # url(r'^invoiceadd/(?P<pk>\d+)/$', views.invoiceform_address_edit, name='invoiceform_address_edit')
]