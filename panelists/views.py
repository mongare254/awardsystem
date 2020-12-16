from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import winner
from user.models import Nominee,Award
from myadmin.models import asession
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required()
def home(request):
    award=Award.objects.all()
    nominees=Nominee.objects.all().order_by('award')
    nominee_name=Nominee.objects.values_list('nominee_name',flat=True)
    count=Nominee.objects.count()
    session=asession.objects.filter(is_active=True)

    return render(request, 'panelist/home.html',{'nominees':nominees,'count':count, 'session':session, 'award':award, 'names':nominee_name})

@login_required()
def history(request):
    winners=winner.objects.all()
    return render(request, 'panelist/history.html', {'winners':winners})

def submit(request):
    if request.method=='POST':
        award = request.POST['award']
        position = request.POST['position']
        description = request.POST['description']
        nominee_name = request.POST['nominee_name']
        c=winner(winner_name=nominee_name,award=award,position=position,description=description)
        try:
            c.save()
            messages.info(request, 'Information submitted successfully')
            return redirect('homepanel')
        except:
            messages.error(request, 'Error submitting information')
            return redirect('homepanel')
    else:
        messages.info(request, 'Unachomaa2')
        return render(request, 'panelist/home.html')

@csrf_exempt
def getnominee(request):
    award_name= request.GET.get('country')
    print(award_name)



