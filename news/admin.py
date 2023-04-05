from django.contrib import admin
from .models import Author, Category, Post, Comment, PostCategory


# admin.site.register(Author)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


# @admin.register(PostCategory)
# class PostCategoryAdmin(admin.ModelAdmin):
#     pass


class PostCategoryInline(admin.TabularInline):
    model = PostCategory


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostCategoryInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass