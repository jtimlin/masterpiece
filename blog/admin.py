from django.contrib import admin
from .models import Painting, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Allows admin to manage categories via the admin panel
    """

    list_display = ('admin', 'name')


@admin.register(Painting)
class PaintingAdmin(SummernoteModelAdmin):
    """
    Allows admin to manage paintings via the admin panel
    """

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'created_on')
    search_fields = ('title', 'content')
    list_filter = ('created_on', 'updated_on')
    summernote_fields = ('description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Allows admin to manage comments on paintings via the admin panel
    """

    list_display = ('name', 'body', 'painting', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')