from django.shortcuts import render
from newsweb.models import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse,request,Http404,FileResponse
import json
from scripts import downloadexcel
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
	id = request.GET['id']
	article = request.GET['article']
	print(id, article)
	if article == 'mondaq':
		data = mondaq.objects.filter(id=id).values()
		excel_name = 'mondaq_'+id
		filepath = downloadexcel.HandleData(data[0],excel_name)
	elif article == 'osac':
		data = osac.objects.filter(id=id)
	elif article == 'grada':
		data = grada.objects.filter(id=id)
	elif article == 'cnn':
		data = cnn.objects.filter(id=id)
	elif article == 'anvilgroup':
		data = anvilgroup.objects.filter(id=id)
	
	file = open(filepath, 'rb')
	response = FileResponse(file)
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="%s.xls"'%excel_name
	return response

# def download(request):
# 	file = open('C:\\Users\Administrator\Desktop\\mondaq_2.xls', 'rb')
# 	response = FileResponse(file)
# 	response['Content-Type'] = 'application/octet-stream'
# 	response['Content-Disposition'] = 'attachment;filename="mondaq_2.xls"'
# 	return response

def download_file(request):
    file = open('/home/logs/log.txt', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="log.txt"'
    return response

def api_delete_article():
	pass

