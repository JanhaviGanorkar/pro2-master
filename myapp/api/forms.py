from django import forms
from .models import Tweet
from .models import Task
from .models import Comment
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'img']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']
# python manage.py migrate app_name previous_migration_name
