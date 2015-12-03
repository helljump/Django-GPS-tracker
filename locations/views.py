#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = 'helljump'


from django.shortcuts import render
from models import Location
from rest_framework import viewsets
from serializers import LocationSerializer
from rest_framework import generics

from django.shortcuts import render_to_response, redirect
from django.template.loader import render_to_string
from django.template import RequestContext
   

class LocationList(generics.ListCreateAPIView):

    serializer_class = LocationSerializer

    def get_queryset(self):
        user = self.request.user
        return Location.objects.filter(user=user)


def map_view(request):
    #points = Location.objects.filter(user=request.user)
    points = Location.objects.all()[:200]
    return render_to_response('map.html', {'points': points},
        context_instance=RequestContext(request))
