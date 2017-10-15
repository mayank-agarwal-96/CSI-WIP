"""WIP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from complaint.views import (
                    complaint_detail,
                    login_view,                    
                    logout_page,
                    not_approved,
                    reject,
                    resolved,
                    show_complaints,
                    signup)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^show/$', show_complaints, name='all-complaints'),
    url(r'^reject/complaint/(\d{1,2})/$', reject, name='reject-complaint'),
    url(r'^register/$', signup, name='register'),
    url(r'^$', login_view, name='login'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^resolved/complaint/(\d{1,2})/$', resolved, name='resolve-complaint'),
    url(r'^complaint/(\d{1,2})/', complaint_detail, name='complaint-detail'),
    url(r'^not-approved/$', not_approved, name='not-approved'),
]
