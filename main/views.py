from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.
def HomePage(request):
    context = {
        'name'='ben shi'
        'token' = '5'
    }
    return render(request, 'main/home.html', context)

class QuizListView(ListView):
    model = Quiz
    template_name = 'main/assignment.html'

def AssignmentPage(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    context = {'obj': quiz}
    return render(request, 'main/assignment.html', context)

def LeaderBoardPage(request):
    context = {}
    return render(request, 'main/leaderboard.html', context)