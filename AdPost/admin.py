from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from AdPost.models import Comment, Post, User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('login', 'phone_number', 'date_of_birth', 'email')


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'text', 'image', 'author_link', 'comments')
    list_filter = ('create',)

    def author_link(self, obj):
        link = reverse("admin:AdPost_user_change", args=[obj.author_post.pk])

        return format_html(f'<a href="{link}">{obj.author_post}</a>')


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ('author_comment', 'text')
