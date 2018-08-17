# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Dorm, Rating

# Create your views here.

# Returns a search form for the user to fill out.
def search(request):
    return render(request, 'nu_dorm_ratings_app/search.html')


# Basic index login route
def index(request):
    if request.user.is_authenticated:
        return redirect('/nu_dorm_ratings_app/search/')
    else:
        return render(request, 'nu_dorm_ratings_app/login.html')

# The route for login authenication
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('/nu_dorm_ratings_app/search/')
    else:
        return redirect('/nu_dorm_ratings_app/')

# Logout route
def logout(request):
    auth_logout(request)
    return redirect('/nu_dorm_ratings_app/')


# Route for viewing a dorm and all of its related info and ratings
def dorm(request, dorm_id):
    dorm = get_object_or_404(Dorm, pk=dorm_id)
    ratings = Rating.objects.filter(dorm_id=dorm_id)
    avg_rating = "Not Yet Rated"
    if len(ratings):
        avg_rating = 0
        count = 0
        for rating in ratings:
            count += float(rating.rating)
        avg_rating = round(count / len(ratings), 2)
    reviews = ratings.exclude(review="")[:10]

    context = { 'dorm': dorm, 'reviews': reviews, 'avg_rating': avg_rating }
    return render(request, 'nu_dorm_ratings_app/dorm.html', context)

# Shows a dorm rating form to the user
def rate(request, dorm_id):
    dorm = get_object_or_404(Dorm, pk=dorm_id)

    return render(request, 'nu_dorm_ratings_app/rate.html', {'dorm': dorm })

# Endpoint for submitting a rating on a dorm
def submit_rating(request, dorm_id):
    rating = request.POST.get('rating', False)
    review = request.POST.get('review', False)
    dorm = get_object_or_404(Dorm, pk=dorm_id)
    if rating:
        user = get_object_or_404(User, pk=request.user.id)
        print(user)
        rating_row = Rating(dorm=dorm, user=user, rating=rating, review=review or '')
        rating_row.save()
        return HttpResponseRedirect(reverse('nu_dorm_ratings_app:dorm', args=(dorm_id)))
    else:
        return redirect('/nu_dorm_ratings_app/rate/' + dorm_id + '/')

# Search results endpoint
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
        dorms = dorms.filter(price_type=price_type)

    context = {'dorms': dorms }
    return render(request, 'nu_dorm_ratings_app/results.html', context)
