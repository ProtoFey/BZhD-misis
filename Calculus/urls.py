from django.urls import path
from Calculus.views import IndexView, Task1View, Result1View, Task2View, Result2View, InfoTask1View, AboutTeamView, ProjectTargetsView

app_name = 'Calculus'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task1/', Task1View.as_view(), name='task1'),
    path('result1/<int:task_id>/', Result1View.as_view(), name='result1'),
    path('task2/', Task2View.as_view(), name='task2'),
    path('result2/<int:task_id>/', Result2View.as_view(), name='result2'),
    path('info-task1/', InfoTask1View.as_view(), name='info-task'),
    path('about_team/', AboutTeamView.as_view(), name='about-team'),
    path('targets/', ProjectTargetsView.as_view(), name='targets')
]
