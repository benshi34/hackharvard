from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.
class QuizListView(ListView):
    model = Quiz
    template_name = 'main/home.html'

def AssignmentPage(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    context = {'obj': quiz}
    return render(request, 'main/assignment.html', context)

def assignment_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

def LeaderBoardPage(request):
    context = {}
    return render(request, 'main/leaderboard.html', context)