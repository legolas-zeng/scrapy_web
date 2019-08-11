# coding=utf-8
# @author: zenganiu
# @time: 2019/8/11 22:19

from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from newsweb import views

urlpatterns = [
	url(r'^$',views.mondaq),
	url(r'mondaq_list',views.mondaq_list,name='mondaq_list'),
	url(r'osac',views.osac,name='osac'),
	url(r'display$',views.dispaly,name='display'),
	url(r'api_delete_article',views.api_delete_article,name='api_delete_article'),

]