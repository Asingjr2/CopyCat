from django.views import generic
from django.views.generic import View, TemplateView, DetailView, ListView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Forum, Post, Comment, PostVote, CommentVote
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import RegisterForm, LoginForm


# Can change "standard query reference from object_list to whatever as below"
class HomePageView(ListView):
    template_name = "forum/list.html"
    context_object_name= "post_list"

    # Throwing error on my end for comment, but view works
    #Should be first page
    def get_queryset(self):
        # Not sure how to pass below...need to refractor into class createview maybe?  Sending context forward as is creates error
        vote_count = Post.objects.first().votes.count()
        upvotes = Post.objects.first().votes.filter(vote=1).count()
        downvotes = Post.objects.first().votes.filter(vote=-1).count()
        total = upvotes - downvotes
        context = {
            "vc": vote_count,
            "total":total
        }
        print(context)
        return Post.objects.all()


def posttest(request):
    if request.method == "POST":
        try:
            user = request.user
            post = Post.objects.get(id=request.POST["post_id"])
            vote = request.POST["vote_choice"]
            PostVote.objects.create(
                user= user,
                post= post,
                vote= vote
                )
        except:
            print("could not create")
        return redirect("/")

# Detail view containing some specific user data...could evolve to user preferences page
class UserView(DetailView):
    model = User

    def get(self, request):
        user = request.user
        context = {
            "user":user, 
            "test": "test"
        }
        return render(request, "forum/user.html", context)

# Try to use with url para, but page throws error regarding UUID
class CommentDetailView(DetailView):
    model = Comment
    template_name= "forum/comment.html"

# Can ignore as we can use package as recommended


# Not sure how to pass information through that I can access (i.e object_name= my_name) and then just use string injection/interpolation in html
# class MainView(generic.DetailView):
#     template_name = "forum/main.html"
    
