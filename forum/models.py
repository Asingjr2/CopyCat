from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.db import models
from django.db.models import Sum
from django.urls import reverse

from autoslug import AutoSlugField

from base.models import BaseModel


UPVOTE = 1
DOWNVOTE = -1
VOTE_CHOICES = (
    (UPVOTE, '+1'),
    (DOWNVOTE, '-1')
)


class Forum(models.Model):
    slug = models.SlugField(primary_key=True, unique=True)
    moderators = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('forum_detail', args=(self.slug,))


class Post(BaseModel):
    forum = models.ForeignKey(
        Forum,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')

    @property
    def upvotes(self):
        return self.votes.filter(vote=UPVOTE).count()

    @property
    def downvotes(self):
        return self.votes.filter(vote=DOWNVOTE).count()

    @property
    def score(self):
        return self.votes.all().aggregate(Sum('vote'))

    def __str__(self):
        return '{}, {}: {}'.format(self.forum, self.user, self.title)

    def get_absolute_url(self):
        return reverse(
            'post_detail',
            args=(self.forum.slug, self.id, self.slug)
        )


class Comment(BaseModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    body = models.TextField(
        validators=[MaxLengthValidator(500)]
    )

    @property
    def upvotes(self):
        return self.votes.filter(vote=UPVOTE).count()

    @property
    def downvotes(self):
        return self.votes.filter(vote=DOWNVOTE).count()

    @property
    def score(self):
        return self.votes.all().aggregate(models.db.Sum('vote'))

    def __str__(self):
        return '{}: {}'.format(self.user, self.body[:10])

    def get_absolute_url(self):
        return reverse(
            'comment_detail',
            args=(self.post.forum.slug, self.post.id, self.post.slug, self.id)
        )


class PostVote(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name='votes',
        on_delete=models.CASCADE
    )
    vote = models.SmallIntegerField(
        choices=VOTE_CHOICES,
        default=UPVOTE
    )

    class Meta:
        unique_together = (
            ('user', 'post')
        )

    def __str__(self):
        return '{}: {}'.format(self.user, self.vote)


class CommentVote(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    comment = models.ForeignKey(
        Comment,
        related_name='votes',
        on_delete=models.CASCADE
    )
    vote = models.SmallIntegerField(
        choices=VOTE_CHOICES,
        default=UPVOTE
    )

    class Meta:
        unique_together = (
            ('user', 'comment')
        )

    def __str__(self):
        return '{}: {}'.format(self.user, self.vote)
