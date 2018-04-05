from django.test import TestCase

from ..models import Post, Comment, PostVote, CommentVote
from ..factories import (
    ForumFactory,
    PostFactory,
    CommentFactory,
    PostVoteFactory,
    CommentVoteFactory,
    PostVoteFactory, 
    CommentVoteFactory
)

class ForumFactoryTestCase(TestCase):
    def test_factory(self):
        tf = ForumFactory()

        self.assertIsNotNone(tf.slug)


class PostFactoryTestCase(TestCase):
    def test_factory(self):
        tp = PostFactory()

        self.assertIsNotNone(tp.forum)
        self.assertIsNotNone(tp.user)


class CommentFactoryTestCase(TestCase):
    def test_factory(self):
        comment = CommentFactory()

        self.assertIsNotNone(comment.post)
        self.assertIsNone(comment.parent)
        self.assertIsNotNone(comment.user)
        self.assertTrue(len(comment.body) <= 500)


class PostVoteFactoryTestCase(TestCase):
    def test_factory(self):
        tpv = PostVoteFactory()

        self.assertIsNotNone(tpv.user)
        self.assertIsNotNone(tpv.post)
        self.assertIsNotNone(tpv.vote)

class CommentVoteFactoryTestCase(TestCase):
    def test_factory(self):
        tcv = CommentVoteFactory()

        self.assertIsNotNone(tcv.user)
        self.assertIsNotNone(tcv.comment)
        self.assertIsNotNone(tcv.vote)
        