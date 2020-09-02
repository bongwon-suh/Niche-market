from django.urls import path, re_path
from board.views import *
from django.contrib import admin

app_name = 'board'

urlpatterns = [
    path('<int:pk>', BoardView.as_view(), name='board'),
    path('board/<int:fk>>/<int:pk>', BoardViewDV.as_view(), name='board_details'),
    path('<int:fk>>/board_add/', BoardCreateView.as_view(), name="board_add"),
    path('<int:pk>/board_update/', BoardUpdateView.as_view(), name="board_update"),
    path('<int:pk>/board_delete', BoardDeleteView.as_view(), name="board_delete"),
]