from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from board.models import Board, models
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, \
    TodayArchiveView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# TemplateView
class BoardView(ListView):
    template_name = 'board_list.html'
    model = Board
    context_object_name = "boards"
    paginate_by = 10


class BoardViewDV(DetailView):
    template_name = 'board_detail.html'
    model = Board
    context_object_name = 'details'


class BoardCreateView(CreateView):
    model = Board
    template_name = 'board_form.html'
    fields = ['title', 'content', 'owner', 'market']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('board:board')

    def form_valid(self, form):
        return super().form_valid(form)


class BoardUpdateView(UpdateView):
    model = Board
    template_name = 'board_form.html'
    fields = ['title', 'content', 'owner', 'market']  # 폼 모델에 사용할 필드  폼 모델 자동 생성
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('board:board')

    def form_valid(self, form):
        return super().form_valid(form)



class BoardDeleteView(DeleteView):
    model = Board
    success_url = reverse_lazy('board:board')
    template_name = 'board_confirm_delete.html'