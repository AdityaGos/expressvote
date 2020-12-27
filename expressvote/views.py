from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import *
from django.contrib.auth.forms import UserCreationForm
from myapp.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from myapp.decorators import unauthenticated_user,allowed_users
from django.contrib.auth.models import Group
from myapp.forms import myleader

def show_about_page(request):
    # return HttpResponse("This is about page")
    # Creating a dictionary name data
    name = 'Aditya Goswami'
    phoneno = '787878788'
    data = {
        'name': name,  # key:value
        'phone': phoneno
    }
    return render(request, "about.html", data)



def landing(request):
    return render(request, 'landing.html', {})


def show_home_page(request):
    images = Imageleader.objects.all()
    loc = location.objects.all()
    data = {'images': images, 'loc': loc}
    return render(request, "home.html", data)

@login_required(login_url='login')
def show_vote_location(request, lid):
    print(lid)
    loc = location.objects.all()
    loca = location.objects.get(pk=lid)
    images = Imageleader.objects.filter(cat=loca)
    data = {'images': images, 'loc': loc}
    return render(request, "vote.html", data)
@login_required(login_url='login')
def show_cand_info(request, cd):
    print(cd)
    print("Hello")
    images = Imageleader.objects.filter(id=cd)
    loc = location.objects.all()
    data = {'images': images, 'loc': loc}
    return render(request, "candidate.html", data)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def show_vote_page(request):
    images = Imageleader.objects.all()
    loc = location.objects.all()
    data = {'images': images, 'loc': loc}
    return render(request, "vote.html", data)

@unauthenticated_user
def registerpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            check=username[-5:]
            if check=='admin':
                group=Group.objects.get(name='admin')
                user.groups.add(group)
            else:
                group = Group.objects.get(name='user')
                user.groups.add(group)
            messages.success(request, 'Account was created for' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def userpage(request):
    context={}
    return render(request,'accounts/user.html',context)

def my_form(request):
    if request.method == "POST":

        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyForm()
    return render(request, 'cv-form.html', {'form': form})

# def create_poll(request):
#     if request.method == "POST":
#
#         form = mylocation(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = mylocation()
#     return render(request, 'create_poll.html', {'form': form})
def create_poll(request):
    if request.method == "POST":
        form = myleader(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = myleader()
    return render(request, 'create_poll.html', {'form': form})
def success(request):
    return HttpResponse('successfully candidate added')