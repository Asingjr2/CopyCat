from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import View
from django.shortcuts import get_object_or_404, redirect

from .models import (
    Forum,
    Post,
    Comment,
    CommentVote,
    UPVOTE,
    DOWNVOTE
)


class ForumDetailView(DetailView):
    model = Forum


class ForumListView(ListView):
    model = Forum


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'


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
