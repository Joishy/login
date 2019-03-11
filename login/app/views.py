# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def get_name(request):
    return render(request, 'home.html',context=None)

def redirect_view(request):
   # response = redirect('welcome.html')
    return render(request, 'welcome.html')

def register(request):
    return render(request, 'register.html')
