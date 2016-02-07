from __future__ import unicode_literals

from django.db import models
from Projects.models import Project
from time import time

def get_upload_file_name(instance,filename):
	return "uploaded_files/addon_header/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.
class Addon(models.Model):
	javascript = 'javascript'
	css = 'css'
	html = 'markup'
	php = 'php'
	python = 'python'
	code_lang = ((javascript, 'javascript'),(html, 'markup'),(css, 'css'),(php,'php'),(python,'python'))

	title              = models.CharField(max_length=500)
	project_hook       = models.IntegerField()
	sort_index         = models.IntegerField(blank=True,default=1)

	image_visibility   = models.BooleanField()
	image 		       = models.FileField(upload_to=get_upload_file_name,blank=True)
	discription	       = models.TextField(blank=True)

	code_visibility    = models.BooleanField()
	type_of_code	   = models.CharField(max_length=20, choices=code_lang, default=html)
	pre_block	       = models.TextField(blank=True)
	code_block	       = models.TextField(blank=True)
	post_block		   = models.TextField(blank=True)


