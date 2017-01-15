from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django import forms
from django.contrib.auth.models import User

from .models import Complaint

def show_complaints(request):
    all_complaint=Complaint.objects.all().filter(validity=True,resolved=False)
    return render(request,'prints.html',{'complaints' : all_complaint})

def reject(request,get_id):
    get_id=int(get_id)
    remove=Complaint.objects.get(id=get_id)
    remove.validity=False
    remove.save()
    html=remove.validity
    return redirect(show_complaints)

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user1=User()
        user1.username=name
        user1.email=email
        user1.set_password(password)
        user1.save()
        return redirect(show_complaints)
    else:
        return render(request, 'registration/register.html')
