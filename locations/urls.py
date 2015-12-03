#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = "helljump"

from django.conf.urls import patterns, url


urlpatterns = patterns('locations.views',
    url(r'^$', 'map_view')
)
