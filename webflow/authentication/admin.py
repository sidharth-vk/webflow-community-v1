from django.contrib import admin
from .models import *
# Register your models here.
class ChildInline(admin.TabularInline):
    model = user_skills

class ChildInline2(admin.TabularInline):
    model = user_work

class ChildInline3(admin.TabularInline):
    model = user_talsk_about

class ChildInline4(admin.TabularInline):
    model = user_portfolio

class ChildInline5(admin.TabularInline):
    model = user_education



class ParentAdmin(admin.ModelAdmin):
    inlines = [ChildInline,ChildInline2,ChildInline3,ChildInline4,ChildInline5]



admin.site.register(profiles,ParentAdmin)
admin.site.register(skills)
admin.site.register(origaniser)
# admin.site.register(profile_rating)
# admin.site.register(core_team)