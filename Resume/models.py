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
class ProfessionalExperience(models.Model):
	title                      = models.CharField(max_length=500, blank=True)
	company_name       		   = models.CharField(max_length=500, blank=True)
	career_discription	       = models.TextField(blank=True)
	start_date				   = models.DateField(default=date.today, blank=True)
	end_date				   = models.DateField(default=date.today, blank=True)

class Education(models.Model):
	title                      = models.CharField(max_length=500, blank=True)
	school_name       		   = models.CharField(max_length=500, blank=True)
	graduate_date			   = models.DateField(default=date.today, blank=True)

