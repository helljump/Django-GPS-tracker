#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = 'helljump'


import os
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import login
from django.views.generic import TemplateView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
from rest_framework import routers
from locations import views


@api_view(['GET'])
def test_view(request, format=None):
    content = {
        'status': 'welcome'
    }
    return Response(content)


def login_success(request, format=None):
    token, created = Token.objects.get_or_create(user=request.user)
    resp = HttpResponse("success")
    resp.set_cookie("token", token)
    return resp


def login_error(request, format=None):
    return HttpResponse(status=401)
    
        
urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),    
    url(r'^api/locations/$', views.LocationList.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login-success/$', login_success),
    url(r'^login-error/$', login_error),
    url(r'^test-view/$', test_view),
    url(r'^$', include('locations.urls')),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
