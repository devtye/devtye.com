from django.contrib import admin
from .models import Skill, ProfessionalExperience, Education

# Register your models here.
class SkillsAdmin(admin.ModelAdmin):
    #fields = ('title','discription')
    list_display = ['title','slug']

class ProfessionalExperienceAdmin(admin.ModelAdmin):
    #fields = ('title','discription')
    list_display = ['title','company_name','start_date','end_date']

class EducationAdmin(admin.ModelAdmin):
    #fields = ('title','discription')
    list_display = ['title','school_name','graduate_date']

admin.site.register(Education, EducationAdmin)
admin.site.register(ProfessionalExperience, ProfessionalExperienceAdmin)
admin.site.register(Skill, SkillsAdmin)