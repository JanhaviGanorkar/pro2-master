from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task
from .models import Tweet
from django.contrib import admin
from .models import Comment
from .models import Like
from .models import Profile
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'tweet', 'comment', 'created_at')

admin.site.register(Comment, CommentAdmin)


admin.site.register(Task)
admin.site.register(Tweet)
admin.site.register(Like)
admin.site.register(Profile)


