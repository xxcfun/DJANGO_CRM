from django.conf.urls import url
from django.contrib.auth.views import login

from users import views

urlpatterns = [
    # 登录
    url(r'^login/', views.login, name='login'),
    # 登出
    url(r'^logout/', views.logout, name='logout'),
    # 改密
    url(r'^mine/', views.mine, name='mine'),
]