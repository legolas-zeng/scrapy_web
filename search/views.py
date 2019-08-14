from django.shortcuts import render
from newsweb.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect, FileResponse
import json
from search import action
from django.core.urlresolvers import reverse

# Create your views here.


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
		print('+++++',key_word)
		return HttpResponseRedirect(reverse(action.action_search, args=[key_word]))
	
	
@csrf_exempt
def searchpage(request,tempalte='search/searchpage.html'):
	return render(request, tempalte)

@csrf_exempt
def seek(request):
	if request.method == 'POST':
		req = json.loads(request.body)
		return HttpResponseRedirect(reverse(action.action_search, args=[req, ]))