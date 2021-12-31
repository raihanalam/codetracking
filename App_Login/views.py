from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

import App_Login
from .forms import SignUpForm,UserProfileChange,ProfilePic

# Create your views here.
def sign_up(request):

     form = SignUpForm()

     registerd = False
     if request.method == 'POST':
          form = SignUpForm(data=request.POST)

          if form.is_valid():
               form.save()
               registerd = True
     dict = {'form': form,'registerd':registerd}

     return render(request,'App_Login/signup.html',context=dict)

def sign_in(request):
     form = AuthenticationForm()

     if request.method == "POST":
          form = AuthenticationForm(data = request.POST )

          if form.is_valid():
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password')

               user = authenticate(username= username,password = password)

               if user is not None:
                    login(request,user)
                    return HttpResponseRedirect(reverse('index'))

     return render(request,'App_Login/signin.html',context={'form':form})

@login_required
def sign_out(request):
     logout(request)
     return HttpResponseRedirect(reverse('index'))


@login_required
def user_profile(request):
     return render(request,'App_Login/profile.html',context={})


@login_required
def change_profile(request):
     current_user = request.user

     form = UserProfileChange(instance=current_user)
     if request.method == "POST":
          form = UserProfileChange(request.POST, instance = current_user)

          if form.is_valid():
               form.save()
               form = UserProfileChange(instance=current_user)

     return render(request,'App_Login/change_profile.html',context={'form':form})

@login_required
def change_password(request):
     current_user = request.user
     form = PasswordChangeForm(current_user)

     if request.method == "POST":
          form = PasswordChangeForm(current_user,data = request.POST)
          if form.is_valid():
               form.save()

     return render(request,'App_Login/change_password.html',context={'form':form})

@login_required
def add_pro_pic(request):
     form = ProfilePic()

     if request.method == "POST":

          form = ProfilePic(request.POST,request.FILES)

          if form.is_valid():
               user_obj = form.save(commit=False)

               user_obj.user = request.user
               user_obj.save() #commit true default
               return HttpResponseRedirect(reverse('App_Login:profile'))

     return render(request,'App_Login/add_pro_pic.html',context={'form': form})

@login_required
def change_pro_pic(request):
     form = ProfilePic(instance=request.user.user_profile)
     if request.method == "POST":
          form = ProfilePic(request.POST,request.FILES,instance=request.user.user_profile)
          if form.is_valid():
               form.save()
               return HttpResponseRedirect(reverse('App_Login:profile'))

     return render(request,'App_Login/add_pro_pic.html',context={'form': form})









