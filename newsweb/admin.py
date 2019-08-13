from django.contrib import admin
from newsweb.models import *
# Register your models here.

class MondaqAdmin(admin.ModelAdmin):
	list_display = ['url','title','create_date','country','authors','organization']
	list_display_links = ['authors']
	list_filter = ['authors']
	
class OsacAdmin(admin.ModelAdmin):
	list_display = ['url','title','create_date','country','city','travel_level']
	
class GradaAdmin(admin.ModelAdmin):
	list_display = ['url','title','create_date','country','event']
	
	
class CnnAdmin(admin.ModelAdmin):
	list_display = ['url','title','create_date','create_date']
	
class AnvilgroupAdmin(admin.ModelAdmin):
	list_display = ['url','title','create_date','level','country']
	list_display_links = ['level']
	list_filter = ['level']
	
admin.site.register(mondaq,MondaqAdmin)
admin.site.register(osac,OsacAdmin)
admin.site.register(grada,GradaAdmin)
admin.site.register(cnn,CnnAdmin)
admin.site.register(anvilgroup,AnvilgroupAdmin)