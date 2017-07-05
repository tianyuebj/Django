# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    '''用户学习的主题'''
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User)

    def __unicode__(self):
    
        return self.text

class Entry(models.Model):
    '''学到的有关某个主题的具体知识'''
    topic=models.ForeignKey(Topic)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meat:
        verbose_name_plural='entries'

    def __unicode__(self):
        s=self.text
        if len(s)>=50:
            return s[:50] + '...'
        else:
            return s
