from django.conf.urls import url
from django.contrib.auth.views import login

from users import views

urlpatterns = [
    # 登录
    url(r'^login/$', views.login_view, name='login_view'),
    # 登出
    url(r'^logout/$', views.logout_view, name='logout_view'),
    # 看个人
    url(r'^filter/(?P<pk>\d+)/$', views.index_filter, name='index_filter'),
]