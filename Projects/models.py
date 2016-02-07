from __future__ import unicode_literals

from django.db import models
from time import time

def get_upload_file_name(instance,filename):
	return "uploaded_files/project_header/%s_%s" % (str(time()).replace('.','_'), filename)

def get_upload_thumbnail_name(instance,filename):
	return "uploaded_files/project_thumbnail/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.
class Project(models.Model):
	title 			= models.CharField(max_length=500)
	discription		= models.TextField(blank=True)
	header 			= models.FileField(upload_to=get_upload_file_name,blank=True)
	tumbnail		= models.FileField(upload_to=get_upload_thumbnail_name,blank=True)
	tag 			= models.CharField(max_length=200)