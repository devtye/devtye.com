from __future__ import unicode_literals

from django.db import models
from Projects.models import Project
from time import time

def get_upload_file_name(instance,filename):
	return "uploaded_files/addon_header/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.
class Addon(models.Model):

	visibility_bool = (
       (True, 'Show'),
       (False, 'Hide'),
    )

	title = models.CharField(max_length=500)
	project_hook = models.IntegerField()

	image_1_visibility = models.BooleanField()
	image_1 		   = models.ImageField(upload_to=get_upload_file_name)
	discription_1	   = models.TextField(blank=True)

	image_2_visibility = models.BooleanField()
	image_2 		   = models.ImageField(upload_to=get_upload_file_name)
	discription_2	   = models.TextField(blank=True)

	image_3_visibility = models.BooleanField()
	image_3 		   = models.ImageField(upload_to=get_upload_file_name)
	discription_3	   = models.TextField(blank=True)

	image_4_visibility = models.BooleanField()	
	image_4 		   = models.ImageField(upload_to=get_upload_file_name)
	discription_4	   = models.TextField(blank=True)

