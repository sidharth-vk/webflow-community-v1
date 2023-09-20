from django.contrib import admin
from .models import *

class ChildInline(admin.TabularInline):
    model = grp_member
class ChildInline2(admin.TabularInline):
    model = grp_feed
class ChildInline3(admin.TabularInline):
    model = grp_skills
class ChildInline4(admin.TabularInline):
    model = grp_talks_about

class ParentAdmin(admin.ModelAdmin):
    inlines = [ChildInline,ChildInline2,ChildInline3,ChildInline4]


# Register your models here.
admin.site.register(group,ParentAdmin)
admin.site.register(grp_member)