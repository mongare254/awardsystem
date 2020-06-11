from django.shortcuts import render,redirect
from django.contrib import messages
from .models import  Award,Nominee
from myadmin.models import asession

# Create your views here.
def home(request):
    awards =Award.objects.all()
    return render(request, 'user/home.html', {'awards': awards})

def nomin(request):
    if request.method == 'POST':
        session=asession.objects.filter(is_active=True)
        awardname=request.POST['award']
        return render(request,'user/nominate.html',{'award':awardname, 'ses':session})
    else:
        session = asession.objects.filter(is_active=True)
        awardname='PLEASE SELECT AWARD FROM HOME PAGE'
        return render(request, 'user/nominate.html', {'award': awardname, 'ses':session})

def nominate(request):
    if request.method =='POST':
        award_f=request.POST['award']
        # nominee_f= request.POST['nominee_name']
        reason_f = request.POST['reason']
        impact_f=request.POST['impact']
        ses_name=request.POST['ses']
        c=Nominee(award=award_f,reason=reason_f,impact=impact_f,session=ses_name)
        try:
            c.save()
            messages.info(request,'Nomination submitted successfully')
            return redirect('nominate')
        except:
            messages.info(request,'Error submitting Nomination!')
            return redirect('nominate')
    else:
        awardname='PLEASE SELECT AWARD FROM HOME PAGE'
        return render(request, 'user/nominate.html',{'award':awardname})