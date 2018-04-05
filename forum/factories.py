import factory
from factory import fuzzy

from .models import (
    Forum,
    Post,
    Comment,
    PostVote,
    CommentVote
)
from base.factories import BaseModelFactory
from user.factories import UserFactory


VOTE_CHOICES = [-1,1]
# For use with post and comment votes.  Would run test to ensure that total vote count increases or descreases by set amount and never goes below zero

class ForumFactory(BaseModelFactory):
    class Meta:
        model = Forum

    slug = factory.Sequence(lambda n: 'forum-{}'.format(n))


class PostFactory(BaseModelFactory):
    class Meta:
        model = Post

    forum = factory.SubFactory(ForumFactory)
    user = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: 'Post Title {}'.format(n))


class CommentFactory(BaseModelFactory):
    class Meta:
        model = Comment

    post = factory.SubFactory(PostFactory)
    user = factory.SubFactory(UserFactory)
    body = factory.fuzzy.FuzzyText(length=500)


class PostVoteFactory(BaseModelFactory):
    class Meta:
        model = PostVote

    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    vote = factory.fuzzy.FuzzyChoice(VOTE_CHOICES)


class CommentVoteFactory(BaseModelFactory):
    class Meta:
        model = CommentVote

    user = factory.SubFactory(UserFactory)
    comment = factory.SubFactory(CommentFactory)
    vote = factory.fuzzy.FuzzyChoice(VOTE_CHOICES)
