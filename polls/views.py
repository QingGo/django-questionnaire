from django.http import Http404

from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# Create your views here.
from .models import Choice, Question, Questionnaire
from django.db.models import F

from django.utils import timezone

from collections import OrderedDict

from pyecharts import Bar, Pie, Line

import pandas

'''
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_questionnaire_list'

    def get_queryset(self):
        return Questionnaire.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
'''
def index(request):
    latest_questionnaire_list = Questionnaire.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

    return render(request, 'polls/index.html', {
        'latest_questionnaire_list': latest_questionnaire_list,
        'myecharts': {
        }
    })

class DetailView(generic.DetailView):
    model = Questionnaire
    template_name = 'polls/detail.html'
    '''
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
    '''

def results(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id)
    pies_for_questions = []
    total_bar_x = []
    total_bar_y = []
    for question in questionnaire.question_set.all():
        pie_x = []
        pie_y = []
        for choice in question.choice_set.all():
            total_bar_x.append(choice.choice_text)
            total_bar_y.append(choice.votes)
            pie_x.append(choice.choice_text)
            pie_y.append(choice.votes)
        pie = Pie("各选项所占百分比")
        pie.add("", pie_x, pie_y, radius=[30, 75], is_label_show=True)
        pies_for_questions.append(pie.render_embed())

    total_bar=Bar("投票结果总览",width=1000,height=700)
    total_bar.add("各选项投票量",total_bar_x, total_bar_y, mark_line=["average"],
     mark_point=["max", "min"], xaxis_rotate=30)

    return render(request, 'polls/results.html', {
            'questionnaire': questionnaire,
            'myecharts': {
                "total_bar" : total_bar.render_embed(),
                "pies_for_questions": pies_for_questions
            }
        })

'''
class ResultsView(generic.DetailView):
    model = Questionnaire
    template_name = 'polls/results.html'
'''

def vote(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id)
    not_select_error_infos = OrderedDict()
    selected_choices_list = []
    for question in questionnaire.question_set.all():
        try:
            selected_choice = question.choice_set.get(choice_text=request.POST['question'+str(question.id)])
            selected_choices_list.append(selected_choice)
        except (KeyError, Choice.DoesNotExist):
            not_select_error_infos['question'+str(question.id)] = "You didn't select a choice"

    if not_select_error_infos:
        return render(request, 'polls/detail.html', {
            'questionnaire': questionnaire,
            'error_message': not_select_error_infos,
        })
    else:
        for selected_choice in selected_choices_list:
            selected_choice.votes = F('votes') + 1
            selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(questionnaire_id,)))

