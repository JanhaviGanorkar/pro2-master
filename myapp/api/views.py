from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Task, Tweet, Like, Comment
from .forms import TweetForm, TaskForm, UserRegistrationForm, CommentForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import ProfileForm
# from .models import  UserProfileUpdateForm

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the same page after saving
    else:
        form = ProfileForm(instance=request.user.profile)  # Load current user data

    context = {
        'user': request.user,
        'form': form  # Pass form to template
    }
    return render(request, 'profile.html', context)

# def shear_post(request):
# if request.method == "POST":
#     form = ShearPostForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


def upload_profile_image(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'add_profile.html', {'form': form})

def show_profile(request):
    profile_image = Profile.objects.all()
    return render(request, 'profile.html', {'profile_images': profile_image})

# View for listing tasks
def ListTodo(request):
    tasks = Task.objects.all()
    return render(request, 'ListTodo.html', {'tasks': tasks})

# def profile(request):
#     user = 

@login_required
def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('ListTodo')
    else:
        form = TaskForm()
    return render(request, 'addTask.html', {'form': form})
    
def delete_Task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method != "POST":
        task.delete()
        return redirect('ListTodo')
    return render(request, 'task_delete.html', {'task': task})

# View for listing tweets
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})


# def edit_task():

# View for creating a tweet
@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user  # Associate the tweet with the logged-in user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

# View for editing a tweet
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

# View for deleting a tweet
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method != "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def tweet_details(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    comments = tweet.comments.all()  # Fetch comments related to the tweet

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # Link comment to logged-in user
            comment.tweet = tweet  # Associate comment with tweet
            comment.save()
            return redirect('tweet_details', tweet_id=tweet.id)
    else:
        form = CommentForm()
    
    return render(request, 'tweet_details.html', {'tweet': tweet, 'comments': comments, 'form': form})

@login_required
def like_toggle(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    like, created = Like.objects.get_or_create(tweet=tweet, user=request.user)

    if not created:
        # If like already exists, delete it (unlike)
        like.delete()

    return redirect(request.META.get('HTTP_REFERER', 'tweet_list'))

@login_required
def tweet_comment(request, tweet_id):
    # Get the tweet for which the comment is being added
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # Create a Comment instance
            comment.user = request.user       # Associate comment with the logged-in user
            comment.tweet = tweet             # Associate comment with the tweet
            comment.save()
            return redirect('tweet_list')     # Redirect to the tweet list or detail page
    else:
        form = CommentForm()

    return render(request, 'addcomment.html', {'form': form, 'tweet': tweet})

def repost_tweet(request, tweet_id):
    original_tweet = get_object_or_404(Tweet, id=tweet_id)

    # Check if user has already reposted the tweet
    if Tweet.objects.filter(user=request.user, reposted_from=original_tweet).exists():
        return redirect('tweet_list')

    # Create a new tweet with reposted reference
    new_tweet = Tweet.objects.create(
        user=request.user,
        text=original_tweet.text,  # Reposting same content
        photo = original_tweet.photo,
        reposted_from=original_tweet
    )
    return redirect('tweet_add_tweet')

# def log_in(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')  # Redirect to home page after login
#         else:
#             return redirect('login')
#             messages.error(request, "Invalid username or password")

#     return render(request, 'register/login.html')
def logout_view(request):
    logout(request)
    return redirect('home')  # Ensure this points to a valid URL in your URLs list

# def add_friend(Tweet, tweet_id):
    # tweet = get_object_or_404(Tweet, id=tweet_id)