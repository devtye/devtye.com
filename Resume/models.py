from __future__ import unicode_literals

from django.db import models
from time import time
from datetime import date

def get_upload_file_name(instance,filename):
	return "uploaded_files/addon_header/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.
class Skill(models.Model):
	title              = models.CharField(max_length=500)
	slug       		   = models.CharField(max_length=500)

# Create your models here.
MONTH_CHOICES=	(
	(1,"January"), 
	(2,"February"),
	(3,"March"), 
	(4,"April "),
	(5,"May"), 
	(6,"June"), 
	(7,"July"),
	(8,"August"), 
	(9,"September"),
	(10,"October"), 
	(11,"November"),
	(12,"December") 
)
  

class ProfessionalExperience(models.Model):
	title                      = models.CharField(max_length=500, blank=True)
	company_name       		   = models.CharField(max_length=500, blank=True)
	career_discription	       = models.TextField(blank=True)
	start_month				   = models.IntegerField(blank=True,choices=MONTH_CHOICES,default=1)
	start_year 				   = models.IntegerField(blank=True,default=2007)
	currently_working  		   = models.BooleanField(default=False)
	end_month				   = models.IntegerField(blank=True,choices=MONTH_CHOICES,default=1)
	end_year 				   = models.IntegerField(blank=True,default=2007)

class Education(models.Model):
	title                      = models.CharField(max_length=500, blank=True)
	school_name       		   = models.CharField(max_length=500, blank=True)
	graduate_month			   = models.IntegerField(blank=True,choices=MONTH_CHOICES,default=1)
	graduate_year 			   = models.IntegerField(blank=True,default=2007)

