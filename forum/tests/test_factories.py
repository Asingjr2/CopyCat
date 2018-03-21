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
        # TODO


class PostFactoryTestCase(TestCase):
    def test_factory(self):
        tp = PostFactory()

        self.assertIsNotNone(tp.forum)
        self.assertIsNotNone(tp.user)
        #   Not sure how to test tite?  Maybe with regex?
        # TODO


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
        # TODO

class CommentVoteFactoryTestCase(TestCase):
    def test_factory(self):
        tcv = CommentVoteFactory()

        self.assertIsNotNone(tcv.user)
        self.assertIsNotNone(tcv.comment)
        self.assertIsNotNone(tcv.vote)
        # TODO

class PostDownvoteTestCase(TestCase):
   '''
   maybe create fake post...fake post vote...then run test to see if downvote descreased votes total...but was still above 0?
   '''
class PostUpvoteTestCase(TestCase):
       '''
   maybe create fake post...fake post vote...then run test to see if upvote increased votes total...?
   '''