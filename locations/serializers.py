#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = 'helljump'

from rest_framework import serializers
from models import Location

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Location
        fields = ('user', 'lat', 'lng', 'alt', 'time')
