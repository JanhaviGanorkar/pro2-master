from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('ListTodo/', views.ListTodo, name='ListTodo'),
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    # path('login/', views.log_in, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    #  path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('addTask/', views.addTask, name='addTask'),
    path('<int:task_id>/delete_Task/', views.delete_Task, name='delete_Task'),
    path('<int:tweet_id>/tweet_comment/', views.tweet_comment, name='tweet_comment'),
    path('tweet/<int:tweet_id>/', views.tweet_details, name='tweet_details'),
    path('like/<int:tweet_id>/', views.like_toggle, name='like_toggle'),
    path('profile', views.profile, name='profile'),
    path('create_or_update_user_profile', views.create_or_update_user_profile, name='create_or_update_user_profile'),
    path('upload_profile_image', views.upload_profile_image, name='upload_profile_image'),
    path('<int:tweet_id>/tweet_add_tweet', views.repost_tweet, name='tweet_add_tweet'),
]
