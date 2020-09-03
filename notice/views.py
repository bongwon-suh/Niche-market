from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from notice.models import Notice
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
from django.core.paginator import Paginator


# Create your views here.

class NoticeListView(ListView):
    model = Notice
    template_name = 'notice/notice_list'
    paginate_by = 5


class NoticeDetailView(DetailView):
    template_name = 'notice/notice_detail.html'
    model = Notice
    context_object_name = 'board'


class NoticeCreateView(CreateView, LoginRequiredMixin):
    model = Notice
    template_name = 'notice/notice_form.html'
    fields = ['title', 'content', ]
    success_url = reverse_lazy('notice:notice_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class NoticeUpdateView(UpdateView, OwnerOnlyMixin):
    model = Notice
    template_name = 'notice/notice_form.html'
    fields = ['title', 'content', ]
    success_url = reverse_lazy('notice:notice_list')


class NoticeDeleteView(DeleteView, OwnerOnlyMixin):
    model = Notice
    success_url = reverse_lazy('notice:notice_list')
