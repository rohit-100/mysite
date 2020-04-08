from django.shortcuts import render

from django.http import HttpResponse
from .models import Question
from django.shortcuts import render,get_object_or_404
from django.http import Http404


def details(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNOtExist:
    #     raise Http404("question does not exist")
    # return render(request, 'polls/details.html', {'question': question})

    question = get_object_or_404(Question, pk=question_id)
    return  render(request,'polls/details.html',{'question': question})


def result(request, question_id):
    return HttpResponse("you are looking at question result %d" % question_id)


def vote(request, question_id):
    return HttpResponse("you are voting on %d" % question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    context = {'latest_question_list': latest_question_list, }
    # output = ' '.join([q.question_text for q in latest_question_list])
    return render(request, 'polls/index.html', context)
