from django.urls import path 
from . import views 

app_name = "forum"
urlpatterns = [
    # Log_Reg page removed 
    path("", views.HomePageView.as_view(), name="home"), 
    path("user", views.UserView.as_view(), name="user"),
    path("comment/<int:pk>", views.CommentDetailView.as_view(), name="comment_detail"),
    path("post", views.posttest, name="posttest"),

]
