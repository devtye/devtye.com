from django.shortcuts import render
from django.http import Http404

from Projects.models import Project

def index(request):
	projects = Project.objects.all()  
	return render( request, 'projects/index.html',{
			'projects': projects,
		})

def project_detail(request, id):
	try:
		project = Project.objects.get(id=id)
	except Project.DoesNotExist:
		raise Http404('This item does not exist')

	return render(request, 'projects/project_detail.html',{
			'project': project,
		})

	return HttpResponse('<p>In project_detail view with id {0}</p>'.format(id))