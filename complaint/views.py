import datetime
import tweepy

from complaint.models import Complaint, Profile
from complaint.forms import SignUpForm, ProfileForm, LoginForm
from complaint.decorators import user_approved_by_admin
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import logout, login
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect


ckey = settings.TWITTER_CKEY
csecret = settings.TWITTER_CSECRET
atoken = settings.TWITTER_ATOKEN
asecret = settings.TWITTER_ASECRET


@login_required(login_url="/login")
@user_approved_by_admin
def resolved(request, cid):
    cid=int(cid)
    complaint=Complaint.objects.get(id=cid)
    complaint.resolved=True
    compid = complaint.cid
    username = complaint.posted_by
    complaint.save()
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    api = tweepy.API(auth)
    api.update_status("@" + username +" Your complaint with id "+ str(cid) + " is resolved!", in_reply_to_status_id = compid)    
    return redirect(show_complaints)


@login_required(login_url="/login")
@user_approved_by_admin
def complaint_detail(request, cid):
    data = Complaint.objects.get(pk=cid)
    context = {'complaint': data}
    return render(request, 'complaint_detail.html', context)


@login_required(login_url="/login")
@user_approved_by_admin
def show_complaints(request):
    #if user.is_authenticated()

    dept_map = {
        "EDC": "education",
        "CSH": "cosha",
        "HST": "hostel",
        "GEN": "general",
    }

    current_user=request.user
    print current_user
    try:
        name = Profile.objects.get(user=current_user)
    #department=current_user.profile.department
    #print department
        department=name.department
    except:
        department = None
    all_complaint=Complaint.objects.all().filter(validity=True, resolved=False)
    if department is not None:
        all_complaint = all_complaint.filter(Q(department=dept_map[department]) | Q(department=""))
    return render(request, 'prints.html', {'complaints' : all_complaint})


@login_required(login_url="/login")
@user_approved_by_admin
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


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('all-complaints')
        return redirect('login')

    else:
        logout(request)
        return render(request, 'login.html', {'form': LoginForm()})


def signup(request):
    if request.method == "POST":
        userform = SignUpForm( request.POST,prefix="userform")
        profileform = ProfileForm( request.POST,prefix="profileform")

        if userform.is_valid() and profileform.is_valid():
            userform.save()
            username = userform.cleaned_data.get('username')
            raw_password = userform.cleaned_data.get('password1')
            
            department = profileform.cleaned_data.get('department')

            user = authenticate(username=username, password=raw_password)
            profile = Profile(user=user, department=department)
            profile.save()

            login(request, user)
            return redirect('all-complaints')

    else:
        userform = SignUpForm(prefix='userform')
        profileform = ProfileForm(prefix='profileform')

        return render(
                    request, 
                    'register.html', 
                    {'userform': userform, 'profileform': profileform})


def logout_page(request):
    logout(request)
    return redirect(login_view)


def not_approved(request):
    return render(request, 'not_approved.html')


def home(request):
    return render(request, 'home.html')