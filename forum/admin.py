from django.contrib import admin

from .models import Forum, Post, Comment, PostVote, CommentVote


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('slug', 'created_at', 'updated_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('forum', 'user', 'title', 'slug', 'created_at', 'updated_at')
    list_filter = ('forum',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'parent', 'user', 'body', 'created_at', 'updated_at')


@admin.register(PostVote)
class PostVoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'vote', 'created_at', 'updated_at')
    list_filter = ('vote',)


@admin.register(CommentVote)
class CommentVoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'vote', 'created_at', 'updated_at')
    list_filter = ('vote',)
