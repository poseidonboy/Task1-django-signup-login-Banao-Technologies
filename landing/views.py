from django.shortcuts import render
from .forms import signup_form, login_form
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import Newuser


# Create your views here.
def onlanding(request):
    if request.method == "POST":
        fm=login_form(request=request, data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            pword=fm.cleaned_data['password']
            usr= authenticate(username=uname, password=pword)
            if usr is not None:
                login(request, usr)
                group = None
                if usr.groups.exists():
                    group = usr.groups.all()[0].name
                    if group == 'Doctor':
                        return HttpResponseRedirect('/dashdoctor/')
                    if group == 'Patient':
                        return HttpResponseRedirect('/dashpatient/')
        else:
            messages.error(request, "Invalid Credentials!!!")
            return HttpResponseRedirect('/')
    else:
        fm= login_form()
    return render(request, 'login.html', {'form': fm})
   


def signup(request):
    if request.method == "POST":
        fm=signup_form(request.POST, request.FILES)
        print(fm)
        if fm.is_valid():
            user = fm.save()
            group = Group.objects.get(name=request.POST.get('groups'))
            user.groups.add(group)
            messages.success(request, "Account created successfully!!!")
            return HttpResponseRedirect('/')
    else:
        fm= signup_form()
    return render(request, 'signup.html', {'form':fm})

    
def dashboard_doctor(request):
    return render(request, 'dashdoctor.html')

  
def dashboard_patient(request):
    return render(request, 'dashpatient.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


