from django.views import generic
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Forum, Post, Comment, PostVote, CommentVote
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import RegisterForm, LoginForm

def index(request):
    return render(request, "forum/index.html")

class LogRegView(View):
    form_class = RegisterForm
    template_name = "forum/log_reg.html"

    def get(self, request):
        form = self.form_class(None)  # none = not bound
        form2 = LoginForm()
        return render(request, self.template_name, {"form": form, "form2": form2})

    def post(self, request):
        if request.POST["form-type"] == "register":

            form = self.form_class(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                password = form.cleaned_data["password"]
                user.set_password(password)
                user.save()
                print("user created")
                return redirect("log_reg")
            else:
                print("form not valid")
                return redirect("log_reg")

        if request.POST["form-type"] == "login":
            submitted_form = LoginForm(request.POST)
            if submitted_form.is_valid():
                try:
                    username = submitted_form.cleaned_data["username"]
                    password = submitted_form.cleaned_data["password"]
                    user = authenticate(username=username, password=password)
                    print("user authentic")
                except:
                    print("user not authentic")
                    # Can add error message warning then redirect back to with repopulated info
                    return redirect("log_reg")

                if user.is_active:
                    login(request, user)
                    print(request.user.email)
                    return redirect("main")

            return redirect("log_reg")

def post(request):
    print("came to post view")
    return redirect("forum:IndexView")

# Not sure how to pass information through that I can access (i.e object_name= my_name) and then just use string injection/interpolation in html
# class MainView(generic.DetailView):
#     template_name = "forum/main.html"
    
def Main(request):
    return render(request, "forum/main.html", {"user":request.user})
