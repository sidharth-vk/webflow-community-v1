from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from groups.models import *
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.db.models import Q
from datetime import datetime
from event.models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import logout
# Create your views here.

def log_in(request):
    if request.user.is_active:
        messages.warning(request, "your are already logged in")

        return redirect("/")


    else:
        if request.method == "POST":
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request ,username=name, password=passwd)
            if user is not None:
                login(request, user)
                messages.success(request, "logged in")
                return redirect("/")

            else:
                messages.error(request, "invalid username and password")
                a="username and password is error"
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        
        return render(request, "auth/login.html")
    


def register_page(request):
    if request.user.is_active:
        messages.warning(request, "your are already logged in")

        return redirect("/")


    else:
        if request.method == "POST":
            name = request.POST.get('fullname')
            email = request.POST.get('username')
            passwd = request.POST.get('password')
            phone = request.POST.get('phone')
            about = "Hello fellow Webflow enthusiasts! I'm thrilled to be a part of this vibrant community where creativity knows no bounds. I've been on a journey of web design and development for a while now, and Webflow has been my trusty companion throughout. When I'm not crafting pixel-perfect websites, you'll find me exploring new design trends, sipping on a cup of coffee, and occasionally getting lost in the world of typography. I'm here to learn, share, and collaborate with all of you amazing folks. Let's turn ideas into beautiful web realities together!"
            designation = "Member"
            joined = datetime.now().year
            birthplace = "WebFlow Island"


            add_user = User.objects.create_user(username=email, password=passwd)
            add_user.save
            Username = get_object_or_404(User, username=email)
            add_profile = profiles.objects.create(user=Username,name=name,about=about,designation=designation,joined=joined,birthplace=birthplace,email=email,linkedin="#",instagram="#",github="#",dob="Na",gender="Na",phono=phone,price="Free")
            add_profile.save
            user = authenticate(request ,username=email, password=passwd)
            username_instance = profiles.objects.get(user=Username)
            
            coreteam = core_team.objects.all()

            for core_name in coreteam:
                a_username = get_object_or_404(User, username=core_name.name)
                a = profiles.objects.get(user=a_username)
                user_follow.objects.create(follower=username_instance,following=a)


            if user is not None:
                login(request, user)
                messages.success(request, "logged in")
                return redirect("/")

            else:
                messages.error(request, "invalid username and password")
                a="username and password is error"
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    return render(request, "auth/register.html")


@login_required
def profile_page(request):
    return render(request,'profile/profile_page.html')


@login_required
def profile_page_output(request,pk):
    user_profile = profiles.objects.filter(slug=pk)
    user_profile_instance = profiles.objects.get(slug=pk)

    current_user_profile = profiles.objects.get(user=request.user)
    
    for i in user_profile:
        
        ids = i.id
        user_name = i.user
    user_profile_instance = profiles.objects.get(slug=pk)
    skills = user_skills.objects.filter(name=ids)
    talsk_about = user_talsk_about.objects.filter(name=ids)
    user_works = user_work.objects.filter(name=ids)

    groups = grp_member.objects.filter(user=ids)
    groups_member = grp_member.objects.filter(user=ids).count

    

    user_portfolios = user_portfolio.objects.filter(name=ids)
    user_portfolios_total = user_portfolio.objects.filter(name=ids).count

    

    user_follower = user_follow.objects.filter(follower=user_profile_instance)[:20]
    user_following_total = user_follow.objects.filter(follower=user_profile_instance).count


    user_follower_new = user_follow.objects.filter(Q(follower=current_user_profile) & Q(following= user_profile_instance))

    user_follower_total = user_follow.objects.filter(following=user_profile_instance).count


    if request.method == "POST":
        rating = request.POST.get('rating')
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        add_rating = profile_rating.objects.create(user=user_profile_instance,rating=rating,comment=comment,email=email,name=name)
        add_rating.save
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


    ratings = profile_rating.objects.filter(user=user_profile_instance)
    rating_total = profile_rating.objects.filter(user=user_profile_instance).count()
    total_number_of_rating = rating_total
    a=0
    for ratings in ratings:
        a = a + ratings.rating

    if total_number_of_rating != 0:
        total_ratings = a / total_number_of_rating
        
    else:
        total_ratings = 0

    total_rating = format(total_ratings, ".1f")

    advs = adv.objects.all()[:1]

    user_edu = user_education.objects.filter(name=ids)

    context ={
        'user_profile':user_profile,
        "skills":skills,
        'user_works':user_works,
        'talsk_about':talsk_about,
        'groups':groups,
        'groups_member':groups_member,
        "user_portfolios":user_portfolios,
        'user_portfolios_total':user_portfolios_total,
        'user_follower':user_follower,
        'user_following_total':user_following_total,
        'user_follower_new':user_follower_new,
        'user_follower_total':user_follower_total,
        'rating_total':rating_total,
        "total_rating":total_rating,
        'advs':advs,
        'user_edu':user_edu
    }
    return render(request,'profile/profile_page.html',context)




@login_required
def addfriend(request, pk):
    user_profile = profiles.objects.get(slug=pk)
    current_user_profile = profiles.objects.get(user=request.user)

    if not user_follow.objects.filter(follower=current_user_profile,following=user_profile).exists():
        addfollower =  user_follow.objects.create(follower=current_user_profile,following=user_profile)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))




def logout_user(request):
    logout(request)

    return redirect('home')