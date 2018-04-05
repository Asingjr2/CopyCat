from uuid import uuid4

from django.test import Client, TestCase
from django.urls import reverse
from ..factories import CommentFactory, ForumFactory, PostFactory, PostVoteFactory, CommentVoteFactory
from user.factories import UserFactory

#  For use throughout tests...may be bad practice..not sure
class ForumDetailViewTestCase(TestCase):
    def test_200(self):
        tf = ForumFactory()
        url = tf.get_absolute_url()
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
     

class ForumListViewTestCase(TestCase):
    def test_200(self):
        client = Client()
        url = reverse('forum_list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)


class ForumUpdateViewTestCase(TestCase):
    def test_302(self):
        test_forum = ForumFactory()
        url = reverse("forum_moderators_add", args=(test_forum.slug,))
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_200(self):
        test_forum = ForumFactory()
        test_user = UserFactory()
        url = reverse("forum_moderators_add", args=(test_forum.slug,))
        client = Client()
        # not sure why failing
        client.force_login(test_user)
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        

class PostDetailViewTestCase(TestCase):
    def test_200(self):
        tf = ForumFactory()
        tp = PostFactory()
        url = tp.get_absolute_url()
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code,200)


class CommentDetailViewTestCase(TestCase):
    def test_404(self):
        #  Do not understand what is goin on
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
        #   Do not understand what is goin on
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
