from django.urls import path
from .views import *


app_name = 'main'

urlpatterns = [
    path('', HomePage, name='home'),
    path('assignment/', AssignmentPage, name='assignment'),
    path('leaderboard/', LeaderBoardPage, name='leaderboard'),
]