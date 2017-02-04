import tweepy
import hashlib
import datetime
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from complaint.models import Complaint, Profile
from django.contrib.auth.decorators import login_required


ckey="IIrRWz5fhgMj1gjrDKdiikpDX"
csecret="VwwcHWHCGLtTFGMz46aPJZAvHFeiG47rA6xC1o0cYwSCpgZZk3"
atoken="819527335107956737-l3DhAfD6zfMUzxkwGi5i4ahaknjYz3V"
asecret="xtnRXB3XbWx9KwRpmUK5MgEMCgyLS90Qd65fFTHEXA9uy"

@login_required(login_url="/")
def resolved(request,cid):
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    api = tweepy.API(auth)
    cid=int(cid)
    complaint=Complaint.objects.get(id=cid)
    complaint.resolved=True
    compid = complaint.cid
    username = complaint.posted_by
    api.update_status("@" + username +" Your complaint with id "+ str(cid) + " is resolved!", in_reply_to_status_id = compid)
    complaint.save()
    return redirect(show_complaints)

@login_required(login_url="/")
def detail(request, cid):
    data = Complaint.objects.get(pk = cid)
    context = {'complaint': data}
    return render(request,'complaint/complaint.html',context)

@login_required(login_url="/")
def show_complaints(request):
    #if user.is_authenticated()
    all_complaint=Complaint.objects.all().filter(validity=True,resolved=False)
    return render(request,'prints.html',{'complaints' : all_complaint})

@login_required(login_url="/")
def reject(request,get_id):
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    api = tweepy.API(auth)

    get_id=int(get_id)
    remove=Complaint.objects.get(id=get_id)
    cid = remove.cid
    username = remove.posted_by
    api.update_status("@" + username +" Your complaint with id "+ str(get_id) +" is rejected!", in_reply_to_status_id = cid)
    remove.validity=False
    remove.save()
    html=remove.validity
    return redirect(show_complaints)

def signup(request):
    if request.method == "POST":
        name = request.POST.get('user', None)
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
