from django.urls import path, register_converter
from . import views 

app_name = "forum"
urlpatterns = [
    # Log_Reg page removed 
    path("", views.AnonPageView.as_view(), name="anon_home"), 
    path("user_sub", views.UserSubredditsView.as_view(), name="user_subreddits"),
    path("forum/<slug:slug>", views.ForumView.as_view(), name="forum"),
    path("post/<uuid:pk>", views.PostView.as_view(), name="post"),
    path("comment/<uuid:pk>", views.CommentView.as_view(), name="comment"),
    path("create_postvote/<uuid:pk>/<slug:slug>", views.create_postvote, name="create_postvote"),
    # Below tried as last resort
    # path("cprac", views.CPracView.as_view(), name="cprac"),
]
'''
**********************STUCK***********************
/r/<forum>/comments/<post_id>/<post_slug>/downvote
**********************STUCK***********************
got above in URL line but now luck :(
have tried following forms in forum_detail which has list of posts
1)
    <form action="/create_postvote/{{ post.id }}/{{ post.slug }}" method="POST">
        {% csrf_token %}
        <input type="hidden" name="id" value="{{post.user.id}}">
        <input type="hidden" name="slug" value="{{post.slug}}">
        <button class="btn btn-warning">
            <input type="submit" value="DOWNVOTE">
        </button>
    </form>
2)
    <form action="/cprac" method="POST">
        {% csrf_token %}
        <input type="hidden" name="id" value="{{post.user.id}}">
        <input type="hidden" name="slug" value="{{post.slug}}">
        <button class="btn btn-warning">
            <input type="submit" value="DOWNVOTE">
        </button>
    </form>
3) Forms either returned no response or the below....
        AttributeError at / cprac
        'WSGIRequest' object has no attribute 'Post'
'''
