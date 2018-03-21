from django.urls import path

from .views import (
    ForumDetailView,
    ForumListView,
    PostDetailView,
    CommentDetailView,
    CommentUpvoteView,
    CommentDownvoteView,
    # Adding new paths 
    PostUpvoteView, 
    PostDownvoteView,
    
)


urlpatterns = [
    path('comments/<uuid:pk>/upvote/',
         CommentUpvoteView.as_view(),
         name='comment_upvote'),
    path('comments/<uuid:pk>/downvote/',
         CommentDownvoteView.as_view(),
         name='comment_downvote'),
#  Adding post_upvote and down_vote paths
    path('posts/<uuid:pk>/upvote/',
         PostUpvoteView.as_view(),
         name='post_upvote'),
    path('posts/<uuid:pk>/downvote/',
         PostDownvoteView.as_view(),
         name='post_downvote'),
    path('<slug:slug>/',
         ForumDetailView.as_view(),
         name='forum_detail'),
    path('<slug:forum_slug>/<uuid:post_id>/<slug:post_slug>/',
         PostDetailView.as_view(),
         name='post_detail'),
    path('<slug:forum_slug>/<uuid:post_id>/<slug:post_slug>/<uuid:comment_id>/',
         CommentDetailView.as_view(),
         name='comment_detail'),
    path('',
         ForumListView.as_view(),
         name='forum_list'),
        #   Adding user profile url to match view that can be tested
    # path('<uuid:user_id>/profile/',
    #      UserProfileView.as_view(),
    #      name='user_profile'),
]
