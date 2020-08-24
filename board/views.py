from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from board.models import Board

# Create your views here.


class BoardList(ListView):
    model = Board
    template_name = 'board/board_list.html'
    context_object_name = 'boards'
