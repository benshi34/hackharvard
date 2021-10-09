from django.urls import path
from .views import *


app_name = 'main'

urlpatterns = [
    path('', HomePage, name='home'),
    path('assignment/', QuizListView.as_view(), name='assignment'),
    path('assignment/<pk>/', AssignmentPage, name='assignment-view'),
    path('leaderboard/', LeaderBoardPage, name='leaderboard'),
]