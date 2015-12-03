#!/usr/bin/env python
#-*- coding: UTF-8 -*-

__author__ = 'helljump'

from django.db import models
from django.contrib.auth.models import User

 
class Location(models.Model):
    user = models.ForeignKey(User)
    lat = models.FloatField() 
    lng = models.FloatField() 
    alt = models.FloatField() 
    time = models.DateTimeField() 

    def __unicode__(self):
        return "%s at %f,%f" % (self.user, self.lat, self.lng)

    class Meta:
        ordering = ('-time', 'user')
