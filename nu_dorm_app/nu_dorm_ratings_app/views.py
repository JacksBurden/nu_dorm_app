# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Dorm, Rating

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. This is about to be the best fuckin app.")

def search(request):
    return render(request, 'nu_dorm_ratings_app/search.html')

def rate(request, dorm_id):
    return HttpResponse("Rate")

def dorm(request, dorm_id):
    return HttpResponse("Dorm")

def results(request):
    name = request.POST.get('name', '')
    kitchen = request.POST.get('kitchen', False)
    dining_hall = request.POST.get('dining_hall', False)
    gym = request.POST.get('gym', False)
    air_conditioning = request.POST.get('air_conditioning', False)
    price_type = request.POST.get('price_type', False)
    dorms = Dorm.objects.filter(name__contains=name)
    if kitchen:
        dorms = dorms.exclude(kitchen=False)
    if dining_hall:
        dorms = dorms.exclude(dining_hall=False)
    if air_conditioning:
        dorms = dorms.exclude(air_conditioning=False)
    if gym:
        dorms = dorms.exclude(gym=False)
    if price_type:
        dorms = dorms.exclude(price_type=False)

    context = {'dorms': dorms }
    return render(request, 'nu_dorm_ratings_app/results.html', context)
