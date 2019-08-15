from django.contrib import admin
from newsweb.models import *
# Register your models here.

class MondaqAdmin(admin.ModelAdmin):
	list_display = ['id','url','title','create_date']
	# list_display_links = ['id']
	# list_filter = ['id']
	
class OsacAdmin(admin.ModelAdmin):
	list_display = ['url','title','create_date','country','city','travel_level']
	# list_display_links = ['id']
	# list_filter = ['id']
class GradaAdmin(admin.ModelAdmin):
	list_display = ['url','title','create_date','country','event']
	# list_display_links = ['id']
	# list_filter = ['id']
	
class CnnAdmin(admin.ModelAdmin):
	list_display = ['url','title','create_date','create_date']
	# list_display_links = ['id']
	# list_filter = ['id']
class AnvilgroupAdmin(admin.ModelAdmin):
	list_display = ['url','title','create_date','level','country']
	# list_display_links = ['id']
	# list_filter = ['id']
	
admin.site.register(mondaq,MondaqAdmin)
admin.site.register(osac,OsacAdmin)
admin.site.register(grada,GradaAdmin)
admin.site.register(cnn,CnnAdmin)
admin.site.register(anvilgroup,AnvilgroupAdmin)