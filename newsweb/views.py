from django.shortcuts import render
from newsweb.models import mondaq

# Create your views here.


def mondaq_list(request,template="newsweb/mondaq.html"):
	data = mondaq.objects.all().values()
	context = {
		'data': data
	}
	return render(request, template,context)


def osac(request,template="newsweb/osac.html"):
	return render(request, template)

def dispaly(request,template="newsweb/dispaly.html"):
	id = request.GET['id']
	print(id)
	data = mondaq.objects.filter(id=id)
	context = {'data': data}
	return render(request, template, context)

def api_delete_article():
	pass

