from django.urls import path

from .views import (
    ForumDetailView,
    ForumListView,
    ForumUpdateView,
    PostDetailView,
    CommentDetailView,
    CommentUpvoteView,
    CommentDownvoteView,
    PostUpvoteView, 
    PostDownvoteView
)


urlpatterns = [
    path('comments/<uuid:pk>/upvote/',
         CommentUpvoteView.as_view(),
         name='comment_upvote'),
    path('comments/<uuid:pk>/downvote/',
         CommentDownvoteView.as_view(),
         name='comment_downvote'),
    path('posts/<uuid:pk>/upvote/',
         PostUpvoteView.as_view(),
         name='post_upvote'),
    path('posts/<uuid:pk>/downvote/',
         PostDownvoteView.as_view(),
         name='post_downvote'),
    path('<slug:slug>/update/',
         ForumUpdateView.as_view(),
         name='forum_moderators_add'),
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
         name='forum_list')
]
