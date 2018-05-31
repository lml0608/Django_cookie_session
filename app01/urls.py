# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^index/$',views.index),
    url(r'^login/$', views.login),

    url(r'^login_handle/$',views.login_handle),
]
