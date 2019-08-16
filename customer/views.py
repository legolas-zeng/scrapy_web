from django.shortcuts import render
from django.contrib.auth.models import User
from scripts import functions
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse,request,Http404
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def user_list(request,template='customer/userlist.html'):
	'''
	is_staff：判断用户是否拥有网站的管理权限
	is_active：判断是否允许用户登陆，设置为“False”时可以不用删除用户来禁止用户登陆
	'''
	# data = User.objects.all().values()
	# print(request.user)
	data = functions.QueryUserList()
	context = {
		'data':data
	}
	return render(request, template ,context)

def user_add(request,template='customer/userlist.html'):
	pass

@csrf_exempt
def api_lock_user(request):
	if request.method == 'POST':
		req = json.loads(request.body)
		id_list = req.get('id_list')
		print(id_list)
		for id in id_list:
			functions.UpdataUser(id)
	context = {
		'msg': '用户已被锁定',
		'status': 1
	}
	return JsonResponse(context)
