from .models import Reservation
from django.shortcuts import redirect, render
from .forms import ReserveTableForm

from reservation.models import Reservation

def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST' :
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()
            return redirect('qr:qr_list')
    context = {'form' : reserve_form}

    return render(request , 'Reservation/reservation.html' , context)

