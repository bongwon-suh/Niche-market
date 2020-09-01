from django.views.generic import TemplateView
from market.models import Location, Market
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from .forms import SingupForm

from django.views.defaults import permission_denied
from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

class HomeView(TemplateView):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        res = requests.get('https://news.seoul.go.kr/economy/archives/category/nationaleconomy-news_c1/tradition_make_c1/traditioninfo_biz_nationaleconomy-n1')
        soup = BeautifulSoup(res.content, 'html.parser')
        title_data = soup.select('div.post-lst h3.tit')
        ctx = {
            'seoul': title_data
        }
        return render(request, 'home.html', ctx)


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = SingupForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()  # 모델 인스턴스 얻기
        if self.request.user != self.object.owner:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)



