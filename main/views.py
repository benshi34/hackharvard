from django.shortcuts import render
from .models import *

# Create your views here.
def HomePage(request):
    context = {}
    return render(request, 'main/home.html', context)

def AssignmentPage(request):
    context = {}
    return render(request, 'main/assignment.html', context)

def LeaderBoardPage(request):
    context = {}
    return render(request, 'main/leaderboard.html', context)