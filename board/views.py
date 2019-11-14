from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import TemplateView, CreateView
import json

from board.models import Board


class BoardIndex(TemplateView):
    template_name = 'board/board_list.html'


class BoardForm(TemplateView):
    template_name = 'board/board_form.html'


# Ajax 처리
def save_post(request):

    title = request.POST.get('title')
    writer = request.POST.get('writer')
    contents = request.POST.get('contents')
    cre_date = timezone.now()

    Board.objects.create(
        title=title,
        cre_user=writer,
        contents=contents,
        cre_date=cre_date
    )

    result = {
                'result': True,
              }
    return HttpResponse(json.dumps(result), content_type="application/json")


#
# class BoardSave(CreateView):
#     model = Board
#     success_url =
