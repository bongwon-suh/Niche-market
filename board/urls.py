from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from board.views import BoardList


app_name = 'board'
urlpatterns = [
    path('',BoardList.as_view(),name='board_list')
]