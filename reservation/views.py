from django.shortcuts import render
from django.views.generic import * # DayArchiveView, ListView
from .models import ConferenceInfo
# Create your views here.


class ConferenceView(View):
    model = ConferenceInfo
    template_name = 'reservation/conference_list.html'
    context_object_name = "conference_infos"


    def get(self, request, *args, **kwargs):
        yyyymmdd = self.kwargs['yyyymmdd']

        print(self.kwargs['yyyymmdd'])

        conference_infos = ConferenceInfo.objects.all()

        context =  {"list": "list_value",
                "yyyymmdd": yyyymmdd,
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

        context = super().get_context_data(**kwargs)

        context["list"] = "list_value"
        context["yyyymmdd"] = self.request.path

        return context