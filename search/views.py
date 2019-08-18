from django.shortcuts import render
from newsweb.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect, FileResponse
import json
from search import action
# from django.core.urlresolvers import reverse
from django.urls import reverse
from scripts import functions


def ip_search(request):
	if request.method=='GET':
		key_word = request.GET['top-search']
		print(key_word)
		return HttpResponseRedirect(reverse(action.action_search, args=[key_word,]))
	
def page_search(request):
	if request.method=='GET':
		title = request.GET['title']
		source = request.GET['source']
		start = request.GET['start']
		end = request.GET['end']
		
		key_word = {
			'title':title,
			'source':source,
			'start':start,
			'end':end,
		}
		# print('+++++',key_word)
		return HttpResponseRedirect(reverse(action.action_search, args=[key_word]))
	
	
@csrf_exempt
def searchpage(request,tempalte='search/searchpage.html'):
	return render(request, tempalte)

@csrf_exempt
def seek(request):
	if request.method == 'POST':
		req = json.loads(request.body)
		return HttpResponseRedirect(reverse(action.action_search, args=[req, ]))
	

def pagelist(request,template="newsweb/page.html"):
	page = request.GET['page']
	article = request.GET['article']
	DisplayPage = 10
	print(page,article)
	startpage = DisplayPage*int(page)
	endpage = DisplayPage*(int(page)+1)
	data1, data2 = functions.QueryPage(article,startpage,endpage)
	context = {
		'data': data1,
		'count': data2[0].get('count(0)'),
		'pagenext':int(page)+1,
		'article':article,
		# 'is_vip_type':is_vip_type[0].get('is_vip_type'),
	}
	return render(request, template,context)