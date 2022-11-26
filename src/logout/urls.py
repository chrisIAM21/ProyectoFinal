from django.urls import path
from . import views

app_name = 'logout'
urlpatterns = [
    path('',views.user_logout, name='logout'),
]