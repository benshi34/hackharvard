from django.urls import path
from .views import *


app_name = 'main'

urlpatterns = [
    path('', QuizListView.as_view(), name='home'),
    path('assignment/<pk>/', AssignmentPage, name='assignment-view'),
    path('assignment/<pk>/data/', assignment_data_view, name='assignment-data-view'),
    path('leaderboard/', LeaderBoardPage, name='leaderboard'),
    path('assignment/<pk>/save/', save_quiz_view, name='save-view'),
]