
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    
path('',groups,name="groups"),
path('<pk>',groups_view,name="groups_view"),
path('grp_add/<pk>',join_grp,name="join_grp")

] 