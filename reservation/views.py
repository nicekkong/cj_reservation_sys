from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import * # DayArchiveView, ListView
from django.forms import ModelForm

from datetime import datetime

from .forms import ConferenceSaveForm
from .models import ConferenceInfo
# Create your views here.

import functools

class IndexView(TemplateView):
    template_name = 'reservation/index.html'


class TodayView(ListView):
    template_name = 'reservation/conference_list.html'
    context_object_name = 'conference_infos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['date'] = datetime.today().strftime('%Y-%m-%d')
        return context

    def get_queryset(self):
        today = datetime.today().strftime('%Y-%m-%d')
        conference_infos = ConferenceInfo.objects.select_related('room').prefetch_related('members__user')\
            .filter(start_date__contains=today).order_by('start_date')
        return conference_infos


class ConferenceView(View):
    model = ConferenceInfo
    template_name = 'reservation/conference_list.html'
    context_object_name = "conference_infos"


    def get(self, request, *args, **kwargs):
        yyyymmdd = self.kwargs['yyyymmdd']
        test = self.kwargs['test']

        print(self.kwargs['yyyymmdd'])

        conference_infos = ConferenceInfo.objects.all()

        context =  {"list": "list_value",
                "yyyymmdd": yyyymmdd,
                "test": test,
                "conference_infos": conference_infos
                }

        return render(request, self.template_name, context)



class ConferenceDAV(DayArchiveView):
    # model = ConferenceInfo
    # queryset = ConferenceInfo.objects.all() # ORM API를 통해 데이터 쿼리를 컨트롤 할 수 있다.
    date_field = 'start_date'
    template_name = 'reservation/conference_list.html'
    ordering = ['start_date']
    context_object_name = "conference_infos"
    make_object_list = True

    def get_queryset(self):   # queryset 파라메터를 메서드화
        return ConferenceInfo.objects.all()


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)  # 상속받은 템플릿 뷰의 기본 context를 우선 설정한다.

        context["list"] = "list_value"
        context["yyyymmdd"] = self.request.path

        return context


class ConferenceSave(View):
    form = ConferenceSaveForm
    template_name = "reservation/save.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form" : self.form})

    def post(self, request):
       form = ConferenceSaveForm(request.POST)

       if form.is_valid():
           print("True")
           conferenceInfo = form.save(commit=False)
           conferenceInfo.start_date = timezone.now()
           conferenceInfo.end_date = timezone.now()
           conferenceInfo.create_date = timezone.now()
           conferenceInfo.save()

           return redirect('reservation:today')

