from django.shortcuts import render
from django.db import models
from detailsapp.models import UserDetails
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory
from .forms import UserModelForm
# from .forms import ServerNameForm
# from .models import Server

def results(request):
    return render(request, "detailsapp/template/results.html", {})

def home(request):
    return render(request, "detailsapp/template/home.html", {})
    
def userDetails(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            u = form.save()
            sequence = UserDetails.sequence
            users = UserDetails.objects.all()
            return render(request, 'detailsapp/template/display.html', {'users':users})
    else:
        form_class = UserModelForm
        return render(request, 'detailsapp/template/userdetails.html' , {'form':form_class,} )
        
