from django.shortcuts import render
from django.http import Http404

from Projects.models import Project
from Addon.models import Addon

def index(request):
	projects = Project.objects.all()  
	return render( request, 'projects/index.html',{
			'projects': projects,
		})

def project_detail(request, id):
	
	try:
		project = Project.objects.get(id=id)
		addon = Addon.objects.get(project_hook=id)
		addon_exist = True
		print(addon)

	except Project.DoesNotExist:
		raise Http404('This item does not exist')

	except Addon.DoesNotExist:
		addon_exist = False
		print('does not have addon')

	if addon_exist is False:
		return render(request, 'projects/project_detail.html',{
			'project': project,
			'addon_exist' : addon_exist,
		})
	else:
		return render(request, 'projects/project_detail.html',{
			'project': project,
			'addon' : addon,
			'addon_exist' : addon_exist,
		})

	return HttpResponse('<p>In project_detail view with id {0}</p>'.format(id))

def check_visibility(addon_unclensed):
	addon_clensed = []
