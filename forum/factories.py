import factory
import factory.fuzzy

from .models import (
    Forum,
    Post,
    Comment,
    PostVote,
    CommentVote
)
from base.factories import BaseModelFactory
from user.factories import UserFactory


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
    body = factory.fuzzy.FuzzyText(length=20)


class PostVoteFactory(BaseModelFactory):
    class Meta:
        model = PostVote

    # TODO


class CommentVoteFactory(BaseModelFactory):
    class Meta:
        model = CommentVote

    # TODO
