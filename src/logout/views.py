from django.shortcuts import render,redirect
from register.models import *
from django.contrib.auth.forms import UserCreationForm
from register.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# Create your views here.

def user_logout(request):
    logout(request)
    return redirect('/')