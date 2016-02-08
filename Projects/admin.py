from django.contrib import admin
from .models import Project, Addon

# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    #fields = ('title','discription')
    list_display = ['title','discription','header']

# Register your models here.
class AddonsAdmin(admin.ModelAdmin):
    list_display = ['title','project_hook','sort_index']


admin.site.register(Addon, AddonsAdmin)
admin.site.register(Project, ProjectsAdmin)