from django.conf.urls import url 
from . import views 

app_name = "forum"
urlpatterns = [
    # urls shared by everyone with index == login
    url(r'^$', views.views, name="index"), 
    url(r'^post$', views.post, name="post"), 
    url(r'^logout$', views.logout, name="logout"), 

    # urls specific to user to when logged in
    url(r'^(?P<user_name>\d+)$', views.main, name="main"),
    url(r'^(?P<user_name>\d+)/profile$', views.profile, name="profile"),
    url(r'^mail$', views.mail, name="mail"), 
    url(r'^preferences$', views.preferneces, name="preferences")
]
