from django.shortcuts import render
from newsweb.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect, FileResponse,JsonResponse,request,Http404
import json
from scripts import downloadexcel,handletranslate,functions
from scripts.mysql_connect import Rrjc_DB
from newsweb import action
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse


@csrf_exempt
def Login(request,template='newsweb/login.html'):
	msg = ''
	next = request.GET.get('next', '')
	if request.method == 'POST':
		username = request.POST['user']
		password = request.POST['passwd']
		next = request.POST['next']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				if next:
					return HttpResponseRedirect(next)
				return HttpResponseRedirect(reverse('index'))
			else:
				msg = u"用户已禁用"
		else:
			msg = u'用户名或者密码错误'
	context = {
		'msg': msg,
		'next': next,
	}
	return render(request, template, context)
@login_required
def Logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))


def mondaq_list(request,template="newsweb/mondaq.html"):
	data = functions.Query('mondaq')
	context = {
		'data': data
	}
	return render(request, template,context)


def osac_list(request,template="newsweb/osac.html"):
    # data = osac.objects.all().values()
    data = functions.Query('osac')
    context = {
        'data': data
    }
    return render(request, template,context)

def grada_list(request,template="newsweb/grada.html"):
	data = functions.Query('grada')
	context = {
		'data': data
	}
	return render(request, template, context)

def cnn_list(request,template="newsweb/cnn.html"):
	data = functions.Query('cnn')
	context = {
		'data': data
	}
	return render(request, template, context)

def anvilgroup_list(request,template="newsweb/anvilgroup.html"):
	data = functions.Query('anvilgroup')
	context = {
		'data': data
	}
	return render(request, template, context)
    

def dispaly(request,template="newsweb/dispaly.html"):
	id = request.GET['id']
	article = request.GET['article']
	print(id,article)
	if article == 'mondaq':
		# data = mondaq.objects.filter(id=id)
		data, authors, tags = functions.QueryArticle('mondaq',id)
		nav = "mondaq"
	elif article == 'osac':
		data, authors, tags = functions.QueryArticle('osac', id)
		nav = "osac"
	elif article == 'grada':
		data, authors, tags = functions.QueryArticle('grada', id)
		nav = "grada"
	elif article == 'cnn':
		data, authors, tags = functions.QueryArticle('cnn', id)
		nav = "cnn"
	elif article == 'anvilgroup':
		data, authors, tags = functions.QueryArticle('anvilgroup', id)
		nav = "anvilgroup"
	# data = mondaq.objects.filter(id=id)
	context = {'data': data,
	           'nav':nav,
	           'authors':authors,
	           'tags':tags,}
	return render(request, template, context)

@csrf_exempt
def api_download(request):
	id = request.GET['id']
	article = request.GET['article']
	# print(id, article)
	data = functions.QueryTranslation(article, id)
	excel_name = article + '_'+ id
	filepath = downloadexcel.HandleData(data[0], excel_name)
	# if article == 'mondaq':
	# 	data = mondaq.objects.filter(id=id).values()
	# 	excel_name = 'mondaq_'+id
	# 	filepath = downloadexcel.HandleData(data[0],excel_name)
	# elif article == 'osac':
	# 	data = osac.objects.filter(id=id).values()
	# 	excel_name = 'osac_' + id
	# 	filepath = downloadexcel.HandleData(data[0], excel_name)
	# elif article == 'grada':
	# 	data = grada.objects.filter(id=id).values()
	# 	excel_name = 'grada_' + id
	# 	filepath = downloadexcel.HandleData(data[0], excel_name)
	# elif article == 'cnn':
	# 	data = cnn.objects.filter(id=id).values()
	# 	excel_name = 'cnn_' + id
	# 	filepath = downloadexcel.HandleData(data[0], excel_name)
	# elif article == 'anvilgroup':
	# 	data = anvilgroup.objects.filter(id=id).values()
	# 	excel_name = 'anvilgroup_' + id
	# 	filepath = downloadexcel.HandleData(data[0], excel_name)
	
	file = open(filepath, 'rb')
	response = FileResponse(file)
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="%s.xls"'%excel_name
	return response
	
@csrf_exempt
def api_mult_download(request):
	if request.method == 'POST':
		req = json.loads(request.body)
		idlist = req.get('data')
		article = req.get('article')
		filepath,filename = downloadexcel.MultHandleData(idlist,article)
		print(filepath,filename)
		context = {
			'filepath':filepath,
			'filename':filename
		}
	
		return JsonResponse(context)
		

def api_translate(request,tempalte='newsweb/translated.html'):
	id = request.GET['id']
	article = request.GET['article']
	tran_title, tran_content = handletranslate.handledata(id, article)
	context = {
		'req': tran_title,
		'content': tran_content,
	}
	return render(request, tempalte, context)

def download_file(request):
	filepath = request.GET['filepath']
	filename = request.GET['filename']
	print(filepath,filename)
	file = open(filepath, 'rb')
	response = FileResponse(file)
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="%s.xls"'%filename
	return response

	
@csrf_exempt
def api_delete_article(request):
	if request.method == 'POST':
		req = json.loads(request.body)
		print(req)
	return HttpResponse({'status': 1})


def test(request,template="search/test.html"):
	return render(request, template)
	
