from django.urls import path, re_path
from board.views import *
from django.contrib import admin

app_name = 'board'

urlpatterns = [
    path('', BoardView.as_view(), name='board'),
    path('<int:pk>', BoardViewDV.as_view(), name='details'),
    # Example: /board/add
    path('add/', BoardCreateView.as_view(), name="add"),
    # Example: /bookmark/change/
    # path('change/', BoardChange.as_view(), name="change"),
    # # Example: /bookmark/99/update/
    path('<int:pk>/update/', BoardUpdateView.as_view(), name="update"),
    # Example: /bookmark/99/delete/
    path('<int:pk>/delete/', BoardDeleteView.as_view(), name="delete"),
#
]