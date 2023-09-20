
from django.urls import path
from .views import *


urlpatterns = [

path('',all_event,name="all_event"),
path('free',all_event_free,name="all_event_free"),
path('paid',all_event_paid,name="all_event_paid"),
path('details/<pk>',event_detail,name="event_detail"),
path('codemeet',codemeet,name="codemeet")

] 