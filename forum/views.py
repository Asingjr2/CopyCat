from django.views import generic
from django.views.generic import View, TemplateView, DetailView, ListView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Forum, Post, Comment, PostVote, CommentVote
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import RegisterForm, LoginForm


# Serving as entry point until user login status is implemented
class AnonPageView(ListView):
    queryset = Forum.objects.all()
    # Change back to standard "forum_list"
    template_name = "forum/user_subreddits.html"
    context_object_name= "forum_list"

# User page with no subreddit set to home (list of forums)
class UserSubredditsView(ListView):
    queryset = Forum.objects.all()
    template_name = "forum/user_subreddits.html"
    context_object_name = "forum_list"

# Could default to DBZ forum or whatever once set
class ForumView(DetailView):
    model = Forum

class PostView(DetailView):
    model = Post

class CommentView(DetailView):
    model = Comment

# Tried old way and print to see if info as being sent
def create_postvote(request, pk, slug ):
    if request.method == 'POST':
        print(pk)
        print(slug)
        print(request.Post["user"])
        print(request.Post["id"])
        print(request.Post["slug"])
        print(request.Post["downvote"])
        return redirect("user_sub")
'''
**********STUCK ON CREATION PART*******
have not been able to find way to create with using model forms...and 
class CPracView(View):
    def post(self, request):
        if request.method == 'POST':
            print(request.Post["id"])
            print(request.Post["slug"])
            return redirect("user_sub")
            
    def get(self, request):
        forum = Forum.objects.first()
        context = {
            "forum":forum
        }
        return render(request,"forum/forum_detail.html", context )
 
'''

