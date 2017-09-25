# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

def login(request):
    user_list = User.objects.all()
    template = loader.get_template('elapp/index.html')
    context = {
        'user_list' : user_list,
    }
    return HttpResponse(template.render(context, request))

def welcome(request):
    user_list = User.objects.all()
    template = loader.get_template('elapp/welcome.html')
    context = {
        'user_list' : user_list,
    }
    return HttpResponse(template.render(context, request))
