from __future__ import unicode_literals

from django.db import models
from time import time

def get_upload_file_name(instance,filename):
	return "uploaded_files/project_header/%s_%s" % (str(time()).replace('.','_'), filename)

def get_upload_thumbnail_name(instance,filename):
	return "uploaded_files/project_thumbnail/%s_%s" % (str(time()).replace('.','_'), filename)

def get_upload_video_name(instance,filename):
	return "uploaded_files/project_video/%s_%s" % (str(time()).replace('.','_'), filename)

def get_upload_addon_file_name(instance,filename):
	return "uploaded_files/addon_header/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.
class Project(models.Model):
	title 			= models.CharField(max_length=500)
	discription		= models.TextField(blank=True)
	header 			= models.FileField(upload_to=get_upload_file_name,blank=True)
	tumbnail		= models.FileField(upload_to=get_upload_thumbnail_name,blank=True)
	tag 			= models.CharField(max_length=200)



# Create your models here.
class Addon(models.Model):
	javascript = 'javascript'
	css = 'css'
	html = 'markup'
	php = 'php'
	python = 'python'
	code_lang = ((javascript, 'javascript'),(html, 'markup'),(css, 'css'),(php,'php'),(python,'python'))


	## PROJECT - GEN
	title              = models.CharField(max_length=500)
	project_hook       = models.IntegerField()
	sort_index         = models.IntegerField(blank=True,default=1)

	## ADDON IMAGE
	image_visibility   = models.BooleanField()
	image 		       = models.FileField(upload_to=get_upload_addon_file_name,blank=True)
	discription	       = models.TextField(blank=True)

	## ADDON CODE
	code_visibility    = models.BooleanField()
	type_of_code	   = models.CharField(max_length=20, choices=code_lang, default=html)
	pre_block	       = models.TextField(blank=True)
	code_block	       = models.TextField(blank=True)
	post_block		   = models.TextField(blank=True)


	## ADDON VIDEO
	video_visibility   = models.BooleanField(default=False)
	pre_video_block	   = models.TextField(blank=True)
	addon_video 	   = models.FileField(upload_to=get_upload_video_name,blank=True)
	post_video_block   = models.TextField(blank=True)


