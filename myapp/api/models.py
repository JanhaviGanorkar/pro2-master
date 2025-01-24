from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    profile_image = models.ImageField(upload_to='profile_images/', default='media/logo.jpg')

    def __str__(self):
        return self.user.username

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default="Pending")
    img = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        # return f"{self.title} {self.status}"
        return f'{self.user.username} - {self.title} {self.status}'
    

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reposted_from = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL) 
    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
    
    class Meta:
        ordering = ['-created_at']


class Like(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)  # Relationship with Tweet
    user = models.ForeignKey(User, on_delete=models.CASCADE)   # Relationship with User
    created_at = models.DateTimeField(auto_now_add=True)       # Optional: Track when the like was made

    def __str__(self):
        return f'{self.user.username} liked {self.tweet.text[:10]}'
    
class Comment(models.Model):
    tweet  = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Comment kis user ne kiya
    comment = models.TextField(max_length=1000)  # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Comment ka time track karna

    def __str__(self):
        return f'{self.user.username} commented on "{self.tweet.text[:10]}"'
