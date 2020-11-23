from django.conf.urls import url

from business import views

urlpatterns = [
    # 查看商机
    url(r'^$', views.business_list, name='business_list'),
    # 添加商机
    url(r'^add/(?P<pk>\d+)/$', views.business_add, name='business_add'),
    # 查看和修改商机
    url(r'^detail/(?P<pk>\d+)/$', views.business_detail, name='business_detail'),
    # 删除商机
    url(r'^del/(?P<pk>\d+)/$', views.business_delete, name='business_delete'),
    # 添加商机中的商品信息
    # url(r'^add_prod/(?P<pk>\d+)/$', views.bus_add_prod, name='bus_add_prod'),
]
