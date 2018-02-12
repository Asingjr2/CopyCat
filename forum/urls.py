from django.urls import path 
from . import views 

app_name = "forum"
urlpatterns = [
    # Will have general front page to see comments...can merge register/login later
    path("", views.Index, name="index"), 
    # Individual register/login page using django user model
    path("log_reg", views.LogRegView.as_view(), name="log_reg"),
    path("post", views.post, name="post"),
    path("main", views.Main, name="main"),

]
