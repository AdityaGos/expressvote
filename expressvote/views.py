from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import *

def show_about_page(request):
    # return HttpResponse("This is about page")
    # Creating a dictionary name data
    name = 'Aditya Goswami'
    phoneno = '787878788'
    data = {
        'name': name,  # key:value
        'phone': phoneno
    }
    return render(request, "about.html",data)
def landing(request):
    return render(request,'landing.html',{})
def show_home_page(request):
    images=Imageleader.objects.all()
    loc=location.objects.all()
    data={'images':images,'loc':loc}
    return render(request,"home.html",data)
def show_vote_location(request,lid):
    print(lid)

    loc = location.objects.all()
    loca=location.objects.get(pk=lid)
    images = Imageleader.objects.filter(cat=loca)
    data = {'images': images, 'loc': loc}
    return render(request, "home.html", data)

def show_cand_info(request,cd):
    print(cd)
    print("Hello")
    images=Imageleader.objects.filter(id=cd)
    loc = location.objects.all()
    data = {'images': images, 'loc': loc}
    return render(request,"candidate.html",data)