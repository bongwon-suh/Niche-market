from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from board.models import Board, models
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, \
    TodayArchiveView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from mysite.views import OwnerOnlyMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy


# TemplateView
class BoardView(ListView):
    model = Board

    def get(self, request, *args, **kwargs):
        queryset = Board.objects.filter(market_id=kwargs['pk']).order_by('id')
        page = int(request.GET.get('p', 1))
        paginator = Paginator(queryset, 5)
        boards = paginator.get_page(page)

        ctx = {
            'boards': boards,
            'market_fk': kwargs['pk'],

        }
        return render(request, 'board_list.html', ctx)


class BoardViewDV(OwnerOnlyMixin, DetailView):
    template_name = 'market/board_detail.html'
    model = Board
    context_object_name = 'details'


class BoardCreateView(OwnerOnlyMixin, CreateView):
    model = Board
    template_name = 'market/board_form.html'
    fields = ['title', 'content', 'owner', 'market']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('market:home')

    def form_valid(self, form):
        return super().form_valid(form)


class BoardUpdateView(OwnerOnlyMixin, UpdateView):
    model = Board
    template_name = 'market/board_form.html'
    fields = ['title', 'content', 'owner', 'market']  # 폼 모델에 사용할 필드  폼 모델 자동 생성
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('market:home')

    def form_valid(self, form):
        return super().form_valid(form)


class BoardDeleteView(OwnerOnlyMixin, DeleteView):
    model = Board
    success_url = reverse_lazy('market:home')
    template_name = 'market/board_confirm_delete.html'
