from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','content_size', 'created_at', 'updated_at']

    def content_size(self, post):
        return '{}글자'.format(len(post.content))
    content_size.short_description = '글자수'


# admin.site.register(Post, PostAdmin)