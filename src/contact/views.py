from django.shortcuts import render , redirect
from django.core.mail import send_mail , BadHeaderError
from django.http import HttpResponse  , HttpResponseRedirect
from .forms import ContactForm
# Create your views here.


def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['Nombre']
            from_email = form.cleaned_data['Email']
            message = form.cleaned_data['Mensaje']

            try : 
                send_mail(subject,message,from_email,['carloschiva09@gmail.com'])

            except BadHeaderError:
                return HttpResponse('ivalid header') 

            return redirect('contact:send_success')
    

    else:
        form = ContactForm()

    context = {
        'form' : form
    }

    return render(request , 'contact/contact.html' , context)



def send_success(request):
    return HttpResponse('Gracias por tu mensaje.')