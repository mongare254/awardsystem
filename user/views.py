from django.shortcuts import render,redirect
from django.contrib  import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import  Award,Nominee
from myadmin.models import asession

# Create your views here.
@login_required()
def home(request):
    awards =Award.objects.all()
    return render(request, 'user/home.html', {'awards': awards})

@login_required()
def nomin(request):
    if request.method == 'POST':
        users = User.objects.all()
        session=asession.objects.filter(is_active=True)
        awardname=request.POST['award']
        return render(request,'user/nominate.html',{'award':awardname, 'ses':session,'users':users})
    else:
        users = User.objects.all()
        session = asession.objects.filter(is_active=True)
        awardname='PLEASE SELECT AWARD FROM HOME PAGE'
        return render(request, 'user/nominate.html', {'award': awardname, 'ses':session,'users':users})

def nominate(request):
    users = User.objects.all()
    if request.method =='POST':
        award_f=request.POST['award']
        nominee_f= request.POST['nominee_name']
        reason_f = request.POST['reason']
        impact_f=request.POST['impact']
        ses_name=request.POST['ses']
        username= request.user.username
        c=Nominee(award=award_f,reason=reason_f,impact=impact_f,session=ses_name,username=username,nominee_name=nominee_f)
        try:
            nominated=Nominee.objects.filter(username=username,session=ses_name)
            if nominated:
                messages.error(request, 'You can only submit a nomination once')
                return redirect('nominate')
            else:
                c.save()
                messages.info(request,'Nomination submitted successfully')
                return redirect('nominate')
        except:
            messages.info(request,'Error submitting Nomination!')
            return redirect('nominate')
    else:
        users = User.objects.all()
        session = asession.objects.filter(is_active=True)
        awardname='PLEASE SELECT AWARD FROM HOME PAGE'
        return render(request, 'user/nominate.html',{'award':awardname,'ses':session,'users':users})

