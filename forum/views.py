from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views import View
from django.shortcuts import get_object_or_404, redirect

from .mixins import ModeratorRequiredMixin
from .forms import ForumUpdateForm

from .models import (
    Forum,
    Post,
    Comment,
    CommentVote,
    UPVOTE,
    DOWNVOTE,
    PostVote
)


# class UserProfileView(DetailView):
#     model = request.user
#     pk_url_kwarg = 'user_id'
    #  Not sure how to add user

class ForumDetailView(DetailView):
    model = Forum


class ForumListView(ListView):
    model = Forum


class ForumUpdateView(ModeratorRequiredMixin, UpdateView):
    model = Forum
    form_class = ForumUpdateForm

    def get_forum(self):
        return self.get_object()


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    # how do i access passed in parameter?
    print(pk_url_kwarg)


class CommentDetailView(DetailView):
    model = Comment
    pk_url_kwarg = 'comment_id'


class CommentUpvoteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=self.kwargs.get('pk'))

        try:
            comment_vote = CommentVote.objects.get(
                user=self.request.user,
                comment=comment
            )
            comment_vote.vote = UPVOTE
            comment_vote.save()
        except CommentVote.DoesNotExist:
            _ = CommentVote.objects.create(
                user=self.request.user,
                comment=comment,
                vote=UPVOTE
            )

        return redirect(comment.get_absolute_url())


class CommentDownvoteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=self.kwargs.get('pk'))

        try:
            comment_vote = CommentVote.objects.get(
                user=self.request.user,
                comment=comment
            )
            comment_vote.vote = DOWNVOTE
            comment_vote.save()
        except CommentVote.DoesNotExist:
            _ = CommentVote.objects.create(
                user=self.request.user,
                comment=comment,
                vote=DOWNVOTE
            )

        return redirect(comment.get_absolute_url())

class PostUpvoteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs.get('pk'))

        try:
            post_vote = PostVote.objects.get(
                user=self.request.user,
                post=post
            )
            post_vote.vote = UPVOTE
            post_vote.save()
        except PostVote.DoesNotExist:
            _ = PostVote.objects.create(
                user=self.request.user,
                post=post,
                vote=UPVOTE
            )

        return redirect(post.get_absolute_url())


class PostDownvoteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs.get('pk'))

        try:
            post_vote = PostVote.objects.get(
                user=self.request.user,
                post=post
            )
            post_vote.vote = DOWNVOTE
            post_vote.save()
        except PostVote.DoesNotExist:
            _ = PostVote.objects.create(
                user=self.request.user,
                post=post,
                vote=DOWNVOTE
            )

        return redirect(post.get_absolute_url())
