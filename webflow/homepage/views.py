from django.shortcuts import render
from authentication.models import *
from groups.models import *
from event.models import *
# Create your views here.

def home(request):
    total_members = User.objects.all().count()
    total_group = group.objects.all().count()
    total_events = events.objects.all().count()

    groups = group.objects.all().order_by('priority')[:3]
    context = {
        "total_members":total_members,
        "total_group":total_group,
        "total_events":total_events,
        "groups":groups
    }
    return render(request,'index.html',context)


def member(request):
    profile = profiles.objects.all()
    total = profiles.objects.all().count
    context = {
        'profile': profile,
        'total':total
    }
    return render(request,'member.html',context)