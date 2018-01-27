from django.shortcuts import render, redirect, HttpResponse
from .models import Forum, Post, Comment, PostVote, CommentVote
from ..base/models import BaseModel 
from django.contrib import messages

# Create your views here.
# Will probably have to refractor, but I am not comfortable with class based views, yet, so it may be best to get some kind of MVC and then modify

# User not logged in
def index(request):
    print "index view"
    return HttpResponse("Index View Sir")

# Page will exist for functionality and then I would add more complicated jquery 
def reg_log(request):
    print "log_reg view"
    return render("forum/log_reg.html")

# Would take in intial login and registration information as well as search ultimately/ much future state
def post(request):
    print "post view"
    return redirect("/main")

# Specific to the user once logged in
def main(request, user_name):
    print "main view"
    return HttpResponse("main View Sir")

# Would be standard form or html page with some user info already populated through a api pull
def profile(request, user_name):
    print "profile view"
    return HttpResponse("profile View Sir")


# Advanced feature
def mail(request):
    print "mail view"
    return HttpResponse("mail View Sir")

# Advanced feature.  Would be standard form or html page with some user info already populated through a api pull
def preferences(request):
    print "preferences view"
    return HttpResponse("preferences View Sir")

def logout(request):
    print 'logging out'
    request.session.clear()
    return redirect('/')
