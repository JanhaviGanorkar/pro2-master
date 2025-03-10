from django.contrib import admin
from .models import Task, Tweet, Comment, Like, Profile, FriendRequest, Friend

# Comment model ka custom admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'tweet', 'comment', 'created_at')

admin.site.register(Comment, CommentAdmin)

# Baaki models ko register karna
admin.site.register(FriendRequest)
admin.site.register(Task)
admin.site.register(Tweet)
admin.site.register(Like)
admin.site.register(Friend)

# Profile ke liye Friend ka inline setup
class FriendInline(admin.TabularInline):
    model = Friend
    extra = 1
    fk_name = "profile"
class ProfileAdmin(admin.ModelAdmin):
    inlines = [FriendInline]

admin.site.register(Profile, ProfileAdmin)  # Ye inline setup ke sath register ho gaya
