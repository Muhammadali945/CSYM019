from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User,Listings
from datetime import datetime


# Create your views here.
def index(request):
    user = User.objects.all()
    return render(request, "login/index.html", {
        "User" : user 
        
    })

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "login/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "login/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login/login.html", {
                "message": "Invalid username and/or password."
            })

    return render(request, "login/login.html")
    
def add(request):
    if request.method == 'POST':
        owner = request.POST["owner"]
        title = request.POST["title"]
        description = request.POST["description"]
        l = Listings()
        l.owner = owner
        l.title = title
        l.description = description
        l.save()
        return HttpResponseRedirect(reverse("index"))
         
    else: 
        
        the_list = Listings.objects.all()    
        return render(request, "login/add_listing.html" , {
            "listings" : the_list
    })

