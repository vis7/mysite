from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ this will return latest five questions. It will not include question published in future """
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, "polls/detail.html", {'question': question})

# def result(request, question_id):
#     question = Question.objects.get(pk=question_id)
#     return render(request, "polls/results.html", {'question' : question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redirecting to the question_detail with error
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You did't selected appropriate choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))

