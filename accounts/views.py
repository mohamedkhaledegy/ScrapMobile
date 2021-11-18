from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate , login

# Create your views here.

def signup(request):
    if request.method == 'Post':
        form = SignupForm(request.Post)
        if form.is_valid():
            form.save()
            eluser = form.cleaned_data['username']
            elpass = form.cleaned_data['password1']            
            user = authenticate(username=eluser , password=elpass)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
    return render(request , 'registration/signup.html',{'form':form})
            
def profile(request):
    
    return render(request,'registration/profile.html')
