from django.shortcuts import render

# Create your views here.


def all_blogs(request):
    return render(request,'blogs/blogs.html')