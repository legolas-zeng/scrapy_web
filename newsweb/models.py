from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class mondaq(models.Model):
	url = models.CharField(max_length=255, verbose_name="网址")
	url_object_id = models.CharField(max_length=255,verbose_name="网址id")
	title = models.CharField(max_length=255,verbose_name="文章标题")
	# create_date = models.DateTimeField(verbose_name="时间")
	create_date = models.CharField(max_length=255,verbose_name="文章创建时间")
	country = models.CharField(max_length=255,verbose_name="地区")
	authors = models.CharField(max_length=255,verbose_name="文章作者")
	organization = models.CharField(max_length=255,verbose_name="文章所属机构或组织")
	tags = models.CharField(max_length=255,verbose_name="标签")
	content = models.TextField(verbose_name="文章内容")
	
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
	url = models.CharField(max_length=255, verbose_name="网址")
	url_object_id = models.CharField(max_length=255, verbose_name="网址id")
	title = models.CharField(max_length=255, verbose_name="标题")
	abstract = models.TextField(verbose_name="摘要")
	create_date = models.CharField(max_length=255, verbose_name="时间")
	country = models.CharField(max_length=255, verbose_name="地区")
	happen_time = models.CharField(max_length=255,verbose_name="事件的开始时间")
	warning_interval_time = models.CharField(max_length=255,verbose_name="事件的预警时间")
	content = models.TextField(verbose_name="信息")
	event = models.TextField(verbose_name="事件", blank=True, null=True)
	analyze = models.TextField(verbose_name="对事件的分析")
	advice = models.TextField(verbose_name="对事件的建议")
	tags = models.CharField(max_length=255, verbose_name="标签", blank=True, null=True)
	relevant_early_warning = models.TextField(verbose_name="事件的最近相关的预警")
	
	class Meta:
		verbose_name = '文章信息'
		verbose_name_plural = '文章信息详情'
	
	
class cnn(models.Model):
	url = models.CharField(max_length=255, verbose_name="网址")
	url_object_id = models.CharField(max_length=255, verbose_name="网址id")
	title = models.CharField(max_length=255, verbose_name="标题")
	create_date = models.CharField(max_length=255, verbose_name="时间")
	tags = models.CharField(max_length=255, verbose_name="标签", blank=True, null=True)
	content = models.TextField(verbose_name="信息")
	content_text = models.TextField(verbose_name="文本信息")
	
	class Meta:
		verbose_name = '文章信息'
		verbose_name_plural = '文章信息详情'
	
class anvilgroup(models.Model):
	url = models.CharField(max_length=255, verbose_name="网址", blank=True, null=True)
	url_object_id = models.CharField(max_length=255, verbose_name="网址id", blank=True, null=True)
	country = models.CharField(max_length=255, verbose_name="地区",default='')
	title = models.CharField(max_length=255, verbose_name="标题", blank=True, null=True)
	level = models.IntegerField(verbose_name="事件的等级", blank=True, null=True)
	create_date = models.CharField(max_length=255, verbose_name="时间",default='')
	content = models.TextField(verbose_name="信息",default='')
	content_text = models.TextField(verbose_name="文本信息",default='')
	crawl_date = models.CharField(max_length=255,verbose_name="爬取时间",default='')
	
	class Meta:
		verbose_name = '文章信息'
		verbose_name_plural = '文章信息详情'


