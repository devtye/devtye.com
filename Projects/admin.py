from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    #fields = ('title','discription')
    list_display = ['title','discription','header']

admin.site.register(Project, ProjectsAdmin)