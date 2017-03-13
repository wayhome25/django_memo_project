"""django_memo_project URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from memo_app import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^logout/$', auth_views.logout, {'next_page' : '/'}),
    url(r'^login/$', auth_views.login,  {'template_name':'memo_app/login.html'}),
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.post, name='new_memo'),
    url(r'^(?P<memokey>[0-9]+)/modify/$', views.modify, name='modify_memo'),
    url(r'^(?P<memokey>[0-9]+)/delete/$', views.delete, name='delete_memo'),
    url(r'^join/$', views.signup, name='join'),
    url(r'^like/$', views.like, name='like'), #like 추가
]
