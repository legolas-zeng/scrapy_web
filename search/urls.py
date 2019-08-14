# coding=utf-8
# @Time    : 2019/8/14 16:40
# @Author  : zwa
from django.conf.urls import include, url
from search import action

urlpatterns = [
	url(r'^(.+)$', action.action_search)
]