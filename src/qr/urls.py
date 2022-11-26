from django.urls import path
from . import views

app_name = 'qr'

urlpatterns = [
    path('',views.qr_list , name='qr_list' ),
]