from django.shortcuts import render
from django.contrib.auth.models import User
from scripts import functions
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse,request,Http404
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password

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

@csrf_exempt
def api_add_user(request):
	# TODO 这里要关联django的user表的，还没弄
	if request.method == 'POST':
		req = json.loads(request.body)
		print(req)
		UserName = req.get('UserName')
		PassWord = req.get('PassWord')
		Email = req.get('Email')
		vip = req.get('vip')
		is_staff = req.get('is_staff')
		is_active = req.get('is_active')
		check_name = User.objects.filter(username__exact=UserName)
		if not check_name:
			print("通过重名检测")
			user = User.objects.create_user(UserName,'xxxxxxx@qq.com', PassWord)
			id = User.objects.filter(username__exact=UserName).values('id')
			print(id[0].get('id'))
			user.save()
			functions.AddUser(id[0].get('id'),UserName,vip,is_staff,is_active)
			context = {
				'msg': '操作成功！！',
				'status': '1'
			}
		else:
			print("没有通过检测")
			context = {
				'msg': '用户名重复！！',
				'status': '0'
			}
	return JsonResponse(context)

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
			if handle == 'deluser':
				User.objects.filter(id=id).delete()
	context = {
		'msg': '操作成功！！',
		'status': 1
	}
	return JsonResponse(context)

@csrf_exempt
def changepasswd(request,template='customer/changepasswd.html'):
	msg = ''
	if request.method == 'POST':
		print(request)
		passwd = request.GET['old']
		newpasswd = request.GET['new']
		renewpasswd = request.GET['renew']
		username = request.user
		print(passwd,newpasswd,renewpasswd,username)
		user = authenticate(username=username, password=passwd)
		if user is not None:
			if user.is_active:
				if newpasswd != renewpasswd:
					msg = "两次新密码输入的不一样"
				else:
					user.set_password(newpasswd)
					user.save()
					return HttpResponseRedirect(reverse('index'))
					# user = User.objects.get(username=username)
					# if user:
					# 	if check_password(request.POST.get('password'), user.password):
					# 		user.password = make_password(newpasswd)
					# 		user.save()
					# 		return HttpResponseRedirect(reverse('index'))
			else:
				msg = "用户已被禁用"
		else:
			msg = '旧密码错误'
	context = {
		'msg': msg,
	}
		
	return render(request,template, context)

@csrf_exempt
def api_changepasswd(request):
	msg = ''
	status = 0
	if request.method == 'POST':
		req = json.loads(request.body)
		passwd = req.get('old')
		newpasswd = req.get('newpasswd')
		renewpasswd = req.get('renewpasswd')
		username = request.user
		print(passwd, newpasswd, renewpasswd, username)
		user = authenticate(username=username, password=passwd)
		if user is not None:
			if user.is_active:
				print("符合修改密码的条件。。")
				# user.set_password(newpasswd)
				# user.save()
				msg = "修改完成"
				status = 1
				# return HttpResponseRedirect(reverse('index'))
			else:
				msg = "用户已被禁用"
				status = 0
		else:
			msg = '旧密码错误'
			status = 0
	context = {
		'data': msg,
		 'status':status,
	}
	
	return JsonResponse(context)

def user_info(request,template='customer/userinfo.html'):
	return render(request, template)
