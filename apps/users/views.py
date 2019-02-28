from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *

def index(request):
    return render(request, "users/index.html")

def register(request):
    errors = User.objects.validator(request.POST, "registration", "")

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        #Redirect the user back to the  reg/login page to fix the errors
        return redirect("/")
    else:
        pword = request.POST['reg-password']
        hashed = bcrypt.hashpw(pword.encode(), bcrypt.gensalt())
        User.objects.create(email=request.POST['reg-email'], password=hashed.decode(), first_name=request.POST['reg-fname'], last_name=request.POST['reg-lname'])
        thisUser = User.objects.last()
        request.session['user_id'] = thisUser.id
        request.session['user_fname'] = thisUser.first_name
        request.session['user_lname'] = thisUser.last_name
        request.session['user_email'] = thisUser.email
        return redirect("/dashboard")

def login(request):
    errors = User.objects.validator(request.POST, "login", "")

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        #Redirect the user back to the  reg/login page to fix the errors
        return redirect("/")
    else:
        thisUser = User.objects.get(email=request.POST['log-email'])
        request.session['user_id'] = thisUser.id
        request.session['user_fname'] = thisUser.first_name
        request.session['user_lname'] = thisUser.last_name
        request.session['user_email'] = thisUser.email
        return redirect("/dashboard")

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect("/")
    else:
        data = {
        }
        return render(request, "users/dashboard.html", data)

def edit_user(request):
    data = {
        "thisUser": User.objects.get(id=request.session['user_id'])
    }
    return render(request, "users/edit.html", data)

def update(request):
    errors = User.objects.validator(request.POST, "update", request.session['user_email'])

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/edit_user")
    else:
        thisUser = User.objects.get(id=request.session['user_id'])
        thisUser.first_name = request.POST['upd-fname']
        thisUser.last_name = request.POST['upd-lname']
        thisUser.street_address = request.POST['upd-address']
        thisUser.city = request.POST['upd-city']
        thisUser.state = request.POST['upd-state']
        thisUser.zip_code = request.POST['upd-zip']
        thisUser.phone = request.POST['upd-phone']
        thisUser.email = request.POST['upd-email']
        thisUser.save()
        request.session['user_fname'] = thisUser.first_name
        request.session['user_lname'] = thisUser.last_name
        request.session['user_email'] = thisUser.email
        return redirect("/dashboard")

def logout(request):
    request.session.clear()
    return redirect("/")