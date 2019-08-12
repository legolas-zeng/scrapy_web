from django.shortcuts import render
from newsweb.models import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse,request,Http404
import json
# Create your views here.


def mondaq_list(request,template="newsweb/mondaq.html"):
	data = mondaq.objects.all().values()
	context = {
		'data': data
	}
	return render(request, template,context)


def osac_list(request,template="newsweb/osac.html"):
    data = osac.objects.all().values()
    context = {
        'data': data
    }
    return render(request, template,context)

def grada_list(request,template="newsweb/osac.html"):
	return render(request, template)

def cnn_list(request,template="newsweb/osac.html"):
	return render(request, template)

def anvilgroup_list(request,template="newsweb/osac.html"):
	return render(request, template)


def article_list(request,template="newsweb/article_list.html"):
    article_name = request.GET['id']
    print(article_name)
    if article_name == 'mondaq':
        data = mondaq.objects.all().values()
        nav = 'mondaq'
    elif article_name == 'osac':
        data = osac.objects.all().values()
        nav = 'osac'
    elif article_name == 'grada':
        data = grada.objects.all().values()
        nav = 'grada'
    elif article_name == 'cnn':
        data = cnn.objects.all().values()
        nav = 'cnn'
    elif article_name == 'anvilgroup':
        data = anvilgroup.objects.all().values()
        nav = 'anvilgroup'
    context = {
        'data': data,
        'nav': nav,
    }
    return render(request, template,context)
    

def dispaly(request,template="newsweb/dispaly.html"):
	id = request.GET['id']
	article = request.GET['article']
	print(id,article)
	if article == 'mondaq':
		data = mondaq.objects.filter(id=id)
		nav = "mondaq"
	elif article == 'osac':
		data = osac.objects.filter(id=id)
		nav = "osac"
	elif article == 'grada':
		data = grada.objects.filter(id=id)
		nav = "grada"
	elif article == 'cnn':
		data = cnn.objects.filter(id=id)
		nav = "cnn"
	elif article == 'anvilgroup':
		data = anvilgroup.objects.filter(id=id)
		nav = "anvilgroup"
	# data = mondaq.objects.filter(id=id)
	context = {'data': data,
	           'nav':nav}
	return render(request, template, context)

@csrf_exempt
def api_download(request):
	if request.method == 'POST':
		req = json.loads(request.body)
		print(req)
	context = {
		'msg': '下载完成',
		'status': 1
	}
	return JsonResponse(context)

def api_delete_article():
	pass

