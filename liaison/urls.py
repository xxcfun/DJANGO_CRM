from django.conf.urls import url

from liaison import views

urlpatterns = [
    # 查看联系人
    url(r'^$', views.liaison_list, name='liaison_list'),
    # 添加联系人
    url(r'^add/(?P<pk>\d+)/$', views.liaison_add, name='liaison_add'),
    # 修改联系人
    url(r'^detail/(?P<pk>\d+)/$', views.liaison_detail, name='liaison_detail'),
    # 删除联系人
    url(r'^del/(?P<pk>\d+)/$', views.liaison_delete, name='liaison_delete')
]