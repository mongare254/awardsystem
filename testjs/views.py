from django.shortcuts import render

# Create your views here.
def yea(request):
    return render(request, 'testjs/test.html')