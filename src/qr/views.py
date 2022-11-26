
from django.shortcuts import render
from .models import qr
# Create your views here.

def qr_list(request):
    qr_list= qr.objects.get(id=1)
    context = {
        'qr_list' : qr_list
    }
    return render(request , 'qr/qr.html',context)