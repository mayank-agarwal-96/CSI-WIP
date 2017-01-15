from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from complaint.models import Complaint

def index(request):
    all_complaint=Complaint.objects.all()
    context = {'all_complaint' : all_complaint}
    return render(request,'complaint/print.html',context)

def resolved(request,cid):
    cid=int(cid)
    remove=Complaint.objects.get(id=cid)
    remove.resolved=True
    remove.save()
    html=remove.resolved
    return redirect(show_complaints)

def detail(request, cid):
    data = Complaint.objects.get(pk = cid)
    context = {'complaint': data}
    return render(request,'complaint/complaint.html',context)

def show_complaints(request):
    all_complaint=Complaint.objects.all()
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
