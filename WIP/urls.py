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
from complaint.views import show_complaints
from complaint.views import reject, signup
from django.contrib.auth import views as auth_views
from complaint.views import reject
from complaint.views import resolved
from complaint.views import detail, logout_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^show/$',show_complaints),
    url(r'^reject/complaint/(\d{1,2})/$',reject),
    url(r'^register/$',signup),
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^resolved/complaint/(\d{1,2})/$',resolved),
    url(r'^complaint/(\d{1,2})/',detail),
]
