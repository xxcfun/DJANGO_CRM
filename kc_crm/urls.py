"""kc_crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from kc_crm import views

urlpatterns = [
    # 管理员后台
    url(r'^admin/', admin.site.urls),
    # 首页
    url(r'^$', views.index, name='index'),
    # 用户模块
    url(r'^users/', include('users.urls', namespace='users')),
    # 客户模块
    url(r'^customer/', include('customer.urls', namespace='customer')),
    # 联系人模块
    url(r'^liaison/', include('liaison.urls', namespace='liaison')),
    # 客户商机模块
    url(r'^business/', include('business.urls', namespace='business')),
    # 拜访记录模块
    url(r'^record/', include('record.urls', namespace='record'))
]
