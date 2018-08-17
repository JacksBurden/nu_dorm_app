# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.

# User Model
class User(models.Model):
    # Enums for gender
    male = 'M'
    female = 'F'
    other = 'O'
    genders = ((male, 'Male'), (female, "Female"), (other, 'Other'))

    morning_person = 'M'
    night_person = 'N'
    flexible = 'F'
    sleep_habits_choices = ((morning_person, 'Morning Person'), (night_person, 'Night Person'), (flexible, 'Flexible'))

    average = 'A'
    neat = 'N'
    messy = 'M'
    cleanliness_choices = ((average, 'Average'), (neat, 'Neat'), (messy, 'Messy'))

    name = models.CharField(max_length=100)
    email = models.EmailField();
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=genders, default=other)
    major = models.CharField(max_length=100, null=True)
    wants_roommate = models.BooleanField(default=False)
    sleep_habits = models.CharField(max_length=1, choices=sleep_habits_choices, default=flexible)
    description = models.CharField(max_length=255, null=True)
    cleanliness = models.CharField(max_length=1, choices=cleanliness_choices, default=average)

    def __str__(self):
        return self.name


# Model representing a Northeastern Dorm
class Dorm(models.Model):

    standard = 'S'
    economy = 'E'
    enhanced = 'EH'
    price_types = ((standard, 'Standard'), (economy, 'Ecomomy'), (enhanced, 'Enhanced'))

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    air_conditioning = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    dining_hall = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    picture = models.ImageField(null=True)
    price_type = models.CharField(max_length=2, choices=price_types, default=standard)

    def __str__(self):
        return self.name

# Model representing a user rating of a dorm
class Rating(models.Model):
    one_star = '1';
    two_stars = '2'
    three_stars = '3'
    four_stars = '4'
    five_stars = '5'

    ratings = ((one_star, 'One Star'), (two_stars, 'Two Stars'),
                (three_stars, 'Three Stars'), (four_stars, 'Four Stars'),
                    (five_stars, 'Five Stars'))

    user = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, null=True)
    dorm = models.ForeignKey(Dorm, on_delete=models.CASCADE)
    rating = models.CharField(max_length=1, choices=ratings, default=three_stars)
    review = models.CharField(max_length=10000, null=True)
