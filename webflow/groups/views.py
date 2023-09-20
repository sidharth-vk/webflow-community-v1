from django.shortcuts import render
from .models import *
from authentication.models import *
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.db.models import Q

# Create your views here.


def groups(request):
    all_groups = group.objects.all().order_by('priority')
    total_groups = group.objects.all().count
    context = {
        'all_groups':all_groups,
        'total_groups':total_groups
    }
    return render(request,'groups/groups.html',context)


def groups_view(request,pk):
    all_groups = group.objects.filter(slug=pk)
    groups_instance = group.objects.get(slug=pk)
    group_member = grp_member.objects.filter(group=groups_instance)
    group_member_total = grp_member.objects.filter(group=groups_instance).count
    grp_feeds = grp_feed.objects.filter(group=groups_instance)
    grp_skill = grp_skills.objects.filter(group=groups_instance)
    grp_talks_abouts = grp_talks_about.objects.filter(group=groups_instance)
    current_user_profile = profiles.objects.get(user=request.user)


    grp_member_grp = grp_member.objects.filter(Q(user=current_user_profile) & Q(group= groups_instance))

    context = {
        'all_groups':all_groups,
        'group_member':group_member,
        'grp_feeds':grp_feeds,
        'group_member_total':group_member_total,
        "grp_skill":grp_skill,
        'grp_talks_abouts':grp_talks_abouts,
        "grp_member_grp":grp_member_grp
    }
    return render(request,'groups/groups_views.html',context)


def join_grp(request,pk):
    groups_instance = group.objects.get(slug=pk)
    current_user_profile = profiles.objects.get(user=request.user)
    grp_member.objects.create(group=groups_instance,user=current_user_profile)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
