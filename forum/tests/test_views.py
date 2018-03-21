from uuid import uuid4

from django.test import Client, TestCase
from django.urls import reverse

from ..factories import CommentFactory
from user.factories import UserFactory


class ForumDetailViewTestCase(TestCase):
    def test_200(self):
        # TODO
        self.assertTrue(True)


class ForumListViewTestCase(TestCase):
    def test_200(self):
        # TODO
        self.assertTrue(True)


class ForumUpdateViewTestCase(TestCase):
    def test_200(self):
        # TODO
        self.assertTrue(True)


class PostDetailViewTestCase(TestCase):
    def test_200(self):
        # TODO
        self.assertTrue(True)


class CommentDetailViewTestCase(TestCase):
    def test_404(self):
        comment = CommentFactory()
        fake_comment_id = str(uuid4())
        url = reverse(
            'comment_detail',
            args=(
                comment.post.forum.slug,
                str(comment.post.id),
                comment.post.slug,
                fake_comment_id
            )
        )

        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_200(self):
        comment = CommentFactory()
        url = comment.get_absolute_url()

        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)


class CommentUpvoteViewTestCase(TestCase):
    def test_login_redirect(self):
        comment = CommentFactory()
        url = reverse('comment_upvote', args=(str(comment.id),))
        data = {}

        client = Client()
        response = client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_200(self):
        comment = CommentFactory()
        voter = UserFactory()
        url = reverse('comment_upvote', args=(str(comment.id),))
        data = {}

        client = Client()
        client.force_login(voter)
        response = client.post(url, data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(comment.upvotes, 1)


class CommentDownvoteViewTestCase(TestCase):
    def test_login_redirect(self):
        comment = CommentFactory()
        url = reverse('comment_downvote', args=(str(comment.id),))
        data = {}

        client = Client()
        response = client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_200(self):
        comment = CommentFactory()
        voter = UserFactory()
        url = reverse('comment_downvote', args=(str(comment.id),))
        data = {}

        client = Client()
        client.force_login(voter)
        response = client.post(url, data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(comment.downvotes, 1)
