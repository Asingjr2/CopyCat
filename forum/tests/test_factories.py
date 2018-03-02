from django.test import TestCase

from ..factories import CommentFactory


class CommentFactoryTestCase(TestCase):
    def test_factory(self):
        comment = CommentFactory()

        self.assertIsNotNone(comment.post)
        self.assertIsNone(comment.parent)
        self.assertIsNotNone(comment.user)
        self.assertTrue(len(comment.body) <= 50)
