from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from post.views import PostList

app_name = 'post'
urlpatterns = [
    path('',PostList.as_view(), name='post_list')
]