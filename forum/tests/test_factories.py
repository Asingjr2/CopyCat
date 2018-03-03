from django.test import TestCase

from ..factories import (
    ForumFactory,
    PostFactory,
    CommentFactory,
    PostVoteFactory,
    CommentVoteFactory
)


class ForumFactoryTestCase(TestCase):
    def test_factory(self):
        # TODO
        self.assertTrue(True)


class PostFactoryTestCase(TestCase):
    def test_factory(self):
        # TODO
        self.assertTrue(True)


class CommentFactoryTestCase(TestCase):
    def test_factory(self):
        comment = CommentFactory()

        self.assertIsNotNone(comment.post)
        self.assertIsNone(comment.parent)
        self.assertIsNotNone(comment.user)
        self.assertTrue(len(comment.body) <= 50)


class PostVoteFactoryTestCase(TestCase):
    def test_factory(self):
        # TODO
        self.assertTrue(True)


class CommentVoteFactoryTestCase(TestCase):
    def test_factory(self):
        # TODO
        self.assertTrue(True)
