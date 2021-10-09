from .views import *
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', HomePage, name='home'),
    path('assignment', AssignmentPage, name='assignment'),
    path('leaderboard', LeaderBoardPage, name='leaderboard'),
]