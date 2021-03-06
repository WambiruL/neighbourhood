from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email', 'password1','password2']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']

class ProfleUpdateForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=['profile_image', 'bio','neighbourhood']


class BusinessUploadForm(forms.ModelForm):

    class Meta:
        model = Business
        fields = ['name','email','logo','description','owner','neighbourhood']

class PostUploadForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title','image','post','neighbourhood','avatar']


