from uuid import uuid4
from django.test import Client, TestCase
from django.urls import reverse
from ..factories import CommentFactory, ForumFactory, PostFactory, PostVoteFactory, CommentVoteFactory
from user.factories import UserFactory

#  For use throughout tests...may be bad practice..not sure
tf = ForumFactory()
tp = PostFactory()
tpv = PostVoteFactory()
tcv = CommentVoteFactory()

class ForumDetailViewTestCase(TestCase):
    def test_200(self):
        url = tf.get_absolute_url
        client = Client()
        response = client.get(url)
        self.assertTrue(response.status_code == 200, "Site does not exist")
        #  saw your assert code after the fact....is more concise...i guess lol and no error message is needed
        # TODO

class ForumListViewTestCase(TestCase):
    def test_200(self):
        client = Client()
        response = client.get("/")
        self.assertTrue(response.status_code == 200, "Site does not exist")
        # TODO
       
class PostDetailViewTestCase(TestCase):
    def test_200(self):
        # test_slug = Forum.objects.first().slug
        # test_post_id = Post.objects.first().id
        # test_post_slug = Post.objects.first().id
        #  <slug:forum_slug>/<uuid:post_id>/<slug:post_slug>/
        url = "{}/{}/{}/".format(tf.slug, tp.id, tp.slug)
        client = Client()
        response = client.get(url)
        self.assertTrue(response.status_code == 200, "Site does not exist")
        # TODO

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
        #  How can this work without passing any variables...or you did above...let me refactor my stuff
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
