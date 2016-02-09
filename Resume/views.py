from django.shortcuts import render
#from Addon.models import Addon

from django.http import Http404
from Resume.models import ProfessionalExperience, Education, Skill

# Create your views here.
def resume_view(request):
	skills 					= Skill.objects.all()  
	professional_experience = ProfessionalExperience.objects.all()
	schools 				= Education.objects.all() 
	months_list 			= ['','January','February','March','April','May','June','July','August','September','October','November','December']

	for experience in professional_experience:
		experience.start_month = months_list[experience.start_month]
		experience.end_month   = months_list[experience.end_month]

	for school in schools:
		school.graduate_month = months_list[school.graduate_month]


	return render( request, 'resume/resume.html',{
		'skills': skills,
		'professional_experience' : professional_experience,
		'schools': schools,
	})