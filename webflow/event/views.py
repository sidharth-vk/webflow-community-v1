from django.shortcuts import render
from .models import *
from authentication.models import *
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

def all_event(request):
    all_events = events.objects.all()
    all_events_total = events.objects.all().count()
    all_events_free_total = events.objects.filter(entry="Free").count()

    paid_event = all_events_total - all_events_free_total

    context ={
        'all_events':all_events,
        "all_events_total":all_events_total,
        "all_events_free_total":all_events_free_total,
        "paid_event":paid_event
    }
    return render(request,'event/all_event.html',context)

def all_event_free(request):
    all_events = events.objects.filter(entry="Free")
    all_events_total = events.objects.all().count()
    all_events_free_total = events.objects.filter(entry="Free").count()

    paid_event = all_events_total - all_events_free_total

    context ={
        'all_events':all_events,
        "all_events_total":all_events_total,
        "all_events_free_total":all_events_free_total,
        "paid_event":paid_event
    }
    return render(request,'event/all_event.html',context)

def all_event_paid(request):
    all_events = events.objects.exclude(entry="Free").all()
    all_events_total = events.objects.all().count()
    all_events_free_total = events.objects.filter(entry="Free").count()

    paid_event = all_events_total - all_events_free_total

    context ={
        'all_events':all_events,
        "all_events_total":all_events_total,
        "all_events_free_total":all_events_free_total,
        "paid_event":paid_event
    }
    return render(request,'event/all_event.html',context)



def codemeet(request):
    team = core_team.objects.all()
    team_total = core_team.objects.all().count

    event_categorys = event_category.objects.get(slug="code-meet")
    

    event = events.objects.filter(category=event_categorys)
    event_total = events.objects.filter(category=event_categorys).count

    context = {
        'team':team,
        'team_total':team_total,
        'event':event,
        "event_total":event_total
    }
    return render(request,'codemeet/codemeet.html',context)



@login_required
def event_detail(request,pk):
    events_details = events.objects.filter(slug=pk)
    events_instance = events.objects.get(slug=pk)
    user = profiles.objects.get(user=request.user)

    if request.method == "POST":
        team = request.POST.get('team')
        college = request.POST.get('collegename')
        semester = request.POST.get('semester')
        event_registration.objects.create(name=user,event=events_instance,team=team,college=college,semester=semester).save
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



    context ={
        'events_details':events_details
    }
    return render(request,'event/event_details.html',context)

