from django.contrib import admin
from .models import CustomUser, Category, Thread, Post
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Category)
admin.site.register(Thread)
admin.site.register(Post)

class ThreadAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'is_locked', 'created_at']
    list_filter = ['is_locked', 'category']
    search_fields = ['title']

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'thread', 'is_reported', 'created_at']
    list_filter = ['is_reported']
    search_fields = ['content']