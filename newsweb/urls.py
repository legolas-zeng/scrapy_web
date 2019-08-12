# coding=utf-8
# @author: zenganiu
# @time: 2019/8/11 22:19

from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from newsweb import views

urlpatterns = [
	url(r'^$',views.mondaq),
    # 文章列表展示页
	url(r'mondaq_list',views.mondaq_list,name='mondaq_list'),
	url(r'osac_list',views.osac_list,name='osac_list'),
	url(r'grada_list',views.grada_list,name='grada_list'),
	url(r'cnn_list',views.cnn_list,name='cnn_list'),
	url(r'anvilgroup_list',views.anvilgroup_list,name='anvilgroup_list'),
    
    # 文章详情页
	url(r'display$',views.dispaly,name='display'),
	# url(r'article_list$',views.article_list,name='article_list'),
	
	# 功能类
	url(r'api_download',views.api_download,name='api_download'),
	url(r'api_delete_article',views.api_delete_article,name='api_delete_article'),

]