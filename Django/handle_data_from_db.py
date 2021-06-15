# views.py
# ListView의 경우 get_queryset 함수로 데이터를 가져와야 한다.

from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Influencer

import re


class InstaDataView(ListView):
    model = Influencer
    context_object_name = 'insta_data' # context의 변수 이름
    template_name = 'dbtest/test.html'

    # 쿼리문으로 데이터 불러와서 물음표 -> 공백 처리
    def get_queryset(self):
        insta_data = Influencer.objects.values()
        for data in insta_data:
            d = data['username']
            d = re.sub('[?]', ' ', d)
            data['username'] = d

        return insta_data