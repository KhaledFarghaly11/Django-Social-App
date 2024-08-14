from django.contrib import admin
from .models import Profile, Post, LikePost, Followers

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'profile_img', 'location']
    raw_id_fields = ['user']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'image', 'caption', 'created_at']

@admin.register(LikePost)
class LikePostAdmin(admin.ModelAdmin):
    list_display = ['post_id', 'username']

@admin.register(Followers)
class FollowersAdmin(admin.ModelAdmin):
    list_display = ['follower', 'user']
