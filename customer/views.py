from django.shortcuts import render
from django.contrib.auth.models import User
from scripts import functions
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse,request,Http404
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def user_list(request,template='customer/userlist.html'):
	'''
	is_staff：判断用户是否是管理员
	is_active：判断是否允许用户登陆，设置为“False”时可以不用删除用户来禁止用户登陆
	is_vip_type：判断VIP会员的类型，默认都是0
	is_superuser：超级用户，最高权限
	'''
	# data = User.objects.all().values()
	# print(request.user)
	data = functions.QueryUserList()
	context = {
		'data':data
	}
	return render(request, template ,context)

def user_add(request,template='customer/useradd.html'):
	
	return render(request, template)
def api_add_user():
	# TODO 这里要关联django的user表的，还没弄
	pass

@csrf_exempt
def api_handle_user(request):
	if request.method == 'POST':
		req = json.loads(request.body)
		print(req)
		id_list = req.get('id_list')
		handle = req.get('handle')
		'''
		handle 操作分为：
		1、添加用户 adduser
		2、锁定用户 lockuser
		3、解锁用户 unlockuser
		4、删除用户 deluser
		'''
		for id in id_list:
			functions.UpdataUser(id,handle)
			#TODO 操作完customer表还要再操作user表，待续.....
	context = {
		'msg': '操作成功！！',
		'status': 1
	}
	return JsonResponse(context)
