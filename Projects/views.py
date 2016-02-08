from django.shortcuts import render
from django.http import Http404

from Projects.models import Project, Addon
#from Addon.models import Addon

def index(request):
	projects = Project.objects.all()  
	return render( request, 'projects/index.html',{
			'projects': projects,
		})

def project_detail(request, id):
	
	try:
		project = Project.objects.get(id=id)
		addons = Addon.objects.filter(project_hook=id)
		addon_exist = True
		print(addons)

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
		addons = addons.order_by('sort_index')
		return render(request, 'projects/project_detail.html',{
			'project': project,
			'addons' : addons,
			'addon_exist' : addon_exist,
		})

	#return HttpResponse('<p>In project_detail view with id {0}</p>'.format(id))

def check_visibility(addon_unclensed):
	addon_clensed = []
