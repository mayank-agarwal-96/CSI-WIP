from django.shortcuts import render

from .models import Complaint

def show_complaints(request):
    all_complaint=Complaint.objects.all()
    # print all_complaint
    return render(request,'prints.html',{'complaints' : all_complaint})
