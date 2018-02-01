# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response,redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.views.generic import ListView
from .forms import SignupForm,ProfileForm
from django.views.generic import View
#from rest_framework.urls import template_name
from requests.api import request
from django.contrib.auth import authenticate,login
from .models import Profile,Post
#from login.forms import SignupForm
# Create your views here.
def Home(request):
    return render_to_response('home.html')
def Login(request):
    c={}
    return render_to_response('Login.html',c)
@csrf_exempt
def Auth_user(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')
    
def Loggedin(request):
    return render_to_response('loggedin.html',{})

def Invalid_login(request):
    return render_to_response('myaccount.html')

def Logout(request):
    return render_to_response('logout.html')

class UserFormView(View):
    form_class=SignupForm
    #template_name='signup.html'
    
    @csrf_exempt
    def get(self,request):
        form=self.form_class(None) 
        print("form get output"+str(form))
        #return render(request, self.template_name, {'form':form})
    @csrf_exempt
    def post(self,request):
        form=self.form_class(request.POST)
        print("form post output"+str(form))
        if form.is_valid():
            user=form.save(commit=False) 
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            #form.save(user)
            
            #user=authenticate(username=username,password=password)
            
            #if user is not None:
                #if user.is_active:
                    #login(request,user)
                   # return redirect('/home')
            return render(request, 'success.html') 
        else:
            return render(request, 'invalid.html') 
def SaveProfile(request):
    saved=False
    if request.method=="POST":
        MyProfileForm=ProfileForm(request.POST,request.FILES)
        if MyProfileForm.is_valid():
            profile=Profile()
            profile.name=MyProfileForm.cleaned_data['name']
            profile.picture=MyProfileForm.cleaned_data['picture']
            profile.save()
            saved=True
    else:
        MyProfileForm=Profile()
    
    return render_to_response('saved.html')   
                   
        
def My_transactions(request):
    return render_to_response('mytransaction.html') 


#def IndexView(ListView):
   # template_name= 'loggedin.html'
    
    def get_queryset(self):
        return Post.objects.all()
