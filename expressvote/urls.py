"""expressvote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing,name='landing'),
    path('about/', views.show_about_page,name='about'),
    path('home/', views.show_home_page,name='home'),
    path('vote/', views.show_vote_page,name='vote'),
    path('user/', views.userpage,name='user'),
    path('location/<int:lid>/', views.show_vote_location),
    path('candidate/<int:cd>/', views.show_cand_info),
    path('register/', views.registerpage, name="register"),
    path('login/', views.loginpage,name="login"),
    path('logout/', views.logoutUser,name="logout"),
    path('form/', views.my_form, name='form'),
    path('createpoll/', views.create_poll, name="createpoll")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
