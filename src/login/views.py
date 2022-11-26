from django.shortcuts import render,redirect
from register.models import *
from django.contrib.auth.forms import UserCreationForm
from register.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        context = {}
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                try:
                    login(request, user)
                    return redirect('/')
                except:
                    messages.success(request,"Ha ocurrido un error, intenta de nuevo")
                    return render(request,'login/login.html',context)
            else:
                messages.success(request,"Usuario no registrado")
                return render(request,'login/login.html',context)

        return render(request,'login/login.html',context)