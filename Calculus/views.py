from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from Calculus.forms import Task1Form, Task2Form
from Calculus.models import Task1, ResultTask1, Task2, ResultTask2


# Create your views here.

class IndexView(TemplateView):
    template_name = 'Calculus/index.html'


class Task1View(CreateView):
    template_name = 'Calculus/task1.html'
    model = Task1
    form_class = Task1Form

    def get_success_url(self):
        last = Task1.objects.last()
        if not last:
            return reverse_lazy('main:result1', args=(1,))
        else:
            return reverse_lazy('main:result1', args=(last.id,))


class Result1View(TemplateView):
    template_name = 'Calculus/result1.html'

    def get_context_data(self, **kwargs):
        context = super(Result1View, self).get_context_data(**kwargs)
        context['result1'] = ResultTask1.objects.get(task_id=self.kwargs.get('task_id'))
        return context


class Task2View(CreateView):
    template_name = 'Calculus/task2.html'
    model = Task2
    form_class = Task2Form

    def get_success_url(self):
        last = Task2.objects.last()
        if not last:
            return reverse_lazy('main:result2', args=(1,))
        else:
            return reverse_lazy('main:result2', args=(last.id,))


class Result2View(TemplateView):
    template_name = 'Calculus/result2.html'

    def get_context_data(self, **kwargs):
        context = super(Result2View, self).get_context_data(**kwargs)
        context['result2'] = ResultTask2.objects.get(task_id=self.kwargs.get('task_id'))
        return context


class InfoTask1View(TemplateView):
    template_name = 'Calculus/info_task1.html'


class AboutTeamView(TemplateView):
    template_name = 'Calculus/about_team.html'


class ProjectTargetsView(TemplateView):
    template_name = 'Calculus/targets.html'
