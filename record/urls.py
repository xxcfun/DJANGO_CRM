from django.conf.urls import url

from record import views

urlpatterns = [
    # 查看客户拜访记录
    url(r'^$', views.record_list, name='record_list'),
    # 添加客户拜访记录
    url(r'^add/(?P<pk>\d+)/$', views.record_add, name='record_add'),
    # 修改客户拜访记录
    url(r'^detail/(?P<pk>\d+)/$', views.record_detail, name='record_detail'),
    # 删除客户拜访记录
    url(r'^del/(?P<pk>\d+)/$', views.record_delete, name='record_delete')
]