'''
Created on Sep 2, 2017

@author: Rohan
'''

from django.contrib.auth.models import User
from django import forms

class SignupForm(forms.ModelForm):
    #username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username','email','password']
        
class ProfileForm(forms.ModelForm):
    name=forms.CharField(max_length=200)
    picture=forms.ImageField()
    
    
       
