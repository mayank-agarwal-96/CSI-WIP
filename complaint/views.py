from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

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
