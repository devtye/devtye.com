from django.contrib import admin
from .models import Addon

# Register your models here.
class AddonsAdmin(admin.ModelAdmin):
    #fields = ('title','discription')
    list_display = ['title','project_hook','sort_index']

admin.site.register(Addon, AddonsAdmin)