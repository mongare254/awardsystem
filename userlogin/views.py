from django.shortcuts import render
import  datetime
from user.views import  home
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from panelists.models import Panelist
from myadmin.models import asession
from django.http import HttpResponse
# Create your views here.

def loginuser(request):
    if request.method=='POST':
        session=asession.objects.get(is_active=True)
        session_name=session.ses_name
        username=request.POST['username']
        password=request.POST['password']
        user =authenticate(username=username,password=password)
        if user is not None:
            panelists = Panelist.objects.filter(username=username)
            if panelists:
                psass
            else:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request,'INVALID CREDENTIALS')
            now = datetime.datetime.now()
            year = now.year
            return render(request, 'userlogin/login.html', {'year': year})
    else:
        now=datetime.datetime.now()
        year=now.year
        return render(request, 'userlogin/login.html', {'year':year})
def logout_user(request):
    logout(request)
    return redirect('auth:login')
