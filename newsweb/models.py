from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class mondaq(models.Model):
	url = models.CharField(max_length=255, verbose_name="网址")
	url_object_id = models.CharField(max_length=255,verbose_name="网址id")
	title = models.CharField(max_length=255,verbose_name="标题")
	# create_date = models.DateTimeField(verbose_name="时间")
	create_date = models.CharField(max_length=255,verbose_name="时间")
	country = models.CharField(max_length=255,verbose_name="地区")
	authors = models.CharField(max_length=255,verbose_name="作者")
	organization = models.CharField(max_length=255,verbose_name="组织")
	tags = models.CharField(max_length=255,verbose_name="标签")
	content = models.TextField(verbose_name="信息")
	
	class Meta:
		verbose_name = '文章信息'
		verbose_name_plural = '文章信息详情'
	
class osac(models.Model):
    url = models.CharField(max_length=255, verbose_name="网址")
    url_object_id = models.CharField(max_length=255, verbose_name="网址id")
    article_type = models.IntegerField(verbose_name="文章类别")
    create_date = models.CharField(max_length=255, verbose_name="时间")
    title = models.CharField(max_length=255, verbose_name="标题")
    content = models.TextField(verbose_name="信息")
    content_text = models.TextField(verbose_name="文本信息")
    country = models.CharField(max_length=255, verbose_name="地区",blank=True,null=True)
    city = models.CharField(max_length=255,verbose_name="城市",blank=True,null=True)
    location = models.CharField(max_length=255,verbose_name="地点",blank=True,null=True)
    event = models.TextField(verbose_name="事件",blank=True,null=True)
    action = models.TextField(verbose_name="活动",blank=True,null=True)
    tags = models.CharField(max_length=255, verbose_name="标签",blank=True,null=True)
    travel_level = models.IntegerField(verbose_name="级别",blank=True,null=True)
    
    class Meta:
        verbose_name = '文章信息'
        verbose_name_plural = '文章信息详情'
        
class grada(models.Model):
	pass

class cnn(models.Model):
	pass

class anvilgroup(models.Model):
	pass

	


