from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Imageleader


# from .models import Order

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class MyForm(forms.ModelForm):
#
#     class Meta:
#
#         model = MyModel
#         fields = ["fullname", "mobile_number", ]
#         labels = {'fullname': "Name", "mobile_number": "Mobile Number", }

# class mylocation(forms.ModelForm):
#     class Meta:
#         model=location
#         fields = ["title", "description", ]
#         labels = {'title': "title", "description": "description", }

class myleader(forms.ModelForm):
    class Meta:
        model = Imageleader
        fields = ['title', 'description', 'description1', 'manifesto1', 'manifesto2', 'manifesto3', 'party', 'image',
                  'cat']
