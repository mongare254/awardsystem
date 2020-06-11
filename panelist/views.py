import datetime
import pytz
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from user.models import Nominee,Award
from myadmin.models import asession


# converting the timezone
time_zone = pytz.timezone('Africa/Nairobi')
#get naive date
date=datetime.datetime.now().date()
time=datetime.time()
date_time= datetime.datetime.combine(date,time)
date_time=time_zone.localize(date_time)
utc_datetime=date_time.astimezone(pytz.utc)
utc_time=utc_datetime.time()
print(date_time)


# Create your views here.
def home(request):
    award=Award.objects.all()
    time_now=datetime.datetime.now()
    nominees=Nominee.objects.all().order_by('award')
    count=Nominee.objects.count()
    session=asession.objects.filter(is_active=True)


    return render(request, 'panelist/home.html',{'nominees':nominees,'count':count, 'session':session, 'award':award})

def history(request):
    return render(request, 'panelist/history.html')

def submit(request):
    if request.method =='GET':
        award_name=request.GET.get('award')
        nominee=Nominee.objects.filter(award=award_name)
        return JsonResponse({'award':nominee})
