from django.shortcuts import render,redirect
from authentication.models import *
# Create your views here.
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import user_passes_test

def organizers(user):
    profile_instance = profiles.objects.get(user=user)
    origanisers = origaniser.objects.filter(user=profile_instance)

    return origanisers


@login_required
@user_passes_test(organizers, login_url='/')
def dashboard(request):
    profile = profiles.objects.all()
    context = {
        "profile":profile
    }
    return render(request,'dashboard/index.html',context)