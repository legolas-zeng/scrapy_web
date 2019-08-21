# coding=utf-8
# @author: zenganiu
# @time: 2019/8/11 22:19

from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from newsweb import views
from search import views as sv
from customer import views as cv
from newsweb import action
urlpatterns = [
	# 首页
	url(r'^$',views.mondaq_list,name='index'),
	
    # 文章列表展示页
	url(r'mondaq_list$',views.mondaq_list,name='mondaq_list'),
	url(r'osac_list',views.osac_list,name='osac_list'),
	url(r'grada_list',views.grada_list,name='grada_list'),
	# url(r'grada_display',views.grada_display,name='grada_display'),
	url(r'cnn_list',views.cnn_list,name='cnn_list'),
	url(r'anvilgroup_list',views.anvilgroup_list,name='anvilgroup_list'),
	url(r'chinhphu_list',views.chinhphu_list,name='chinhphu_list'),
	url(r'anvilgroup_list',views.anvilgroup_list,name='anvilgroup_list'),
	url(r'pagelist',sv.pagelist,name='pagelist'),
	

    # 文章详情页
	url(r'display$',views.dispaly,name='display'),
	# url(r'article_list$',views.article_list,name='article_list'),
	
	# 功能类
	url(r'api_download',views.api_download,name='api_download'),
	url(r'api_mult_download',views.api_mult_download,name='api_mult_download'),
	url(r'api_translate',views.api_translate,name='api_translate'),
	url(r'download_file',views.download_file,name='download_file'),
	url(r'test',views.test,name='test'),
	
	# 操作类接口
	url(r'api_delete_article',views.api_delete_article,name='api_delete_article'),
	
	# 权限类
	url(r'^login$',views.Login,name='login'),
	url(r'^logout', views.Logout, name='logout'),
	url(r'^changepasswd', cv.changepasswd, name='changepasswd'),
	url(r'^api_changepasswd', cv.api_changepasswd, name='api_changepasswd'),

	
	# 搜索类
	url(r'^ip_search$', sv.ip_search, name='ip_search'),
	url(r'^page_search', sv.page_search, name='page_search'),
	url(r'searchpage',sv.searchpage,name='searchpage'),
	# url(r'seek',sv.seek,name='seek'), # 查询接口
	url(r'^action_search',include('search.urls')),
	
	# 用户类
	url(r'^user_list', cv.user_list, name='user_list'),
	url(r'^api_handle_user', cv.api_handle_user, name='api_handle_user'),
	url(r'^api_add_user', cv.api_add_user, name='api_add_user'),
	url(r'^user_add', cv.user_add, name='user_add'),
	url(r'^user_info', cv.user_info, name='user_info'),

]